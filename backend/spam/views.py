from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import PhoneNumber
from .serializers import PhoneNumberSerializer

# ✅ ML + GenAI imports
from ml_engine.predict import predict_spam
from ml_engine.explain import generate_explanation


# 🔍 Lookup API
class LookupNumberAPIView(APIView):
    def get(self, request):
        number = request.query_params.get("number")

        if not number:
            return Response({"error": "Number required"}, status=400)

        # Get or create number
        obj, created = PhoneNumber.objects.get_or_create(number=number)

        # 🔥 STEP 1: Prepare dummy text (later we improve)
        text = f"Message from {number}"

        # 🔥 STEP 2: ML Prediction
        score = predict_spam(text)

        # 🔥 STEP 3: GenAI Explanation
        explanation = generate_explanation(score)

        # 🔥 STEP 4: Update DB
        obj.spam_score = score
        obj.is_spam = score > 0.5
        obj.save()

        # 🔥 STEP 5: Serialize + add explanation
        data = PhoneNumberSerializer(obj).data
        data["explanation"] = explanation

        return Response(data)


# 🚨 Report Spam API
class ReportSpamAPIView(APIView):
    def post(self, request):
        number = request.data.get("number")

        if not number:
            return Response({"error": "Number required"}, status=400)

        obj, _ = PhoneNumber.objects.get_or_create(number=number)

        obj.reports += 1
        obj.is_spam = True
        obj.spam_score = min(obj.reports * 0.1, 1.0)

        obj.save()

        return Response({"message": "Reported successfully"})