from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import PhoneNumber
from .serializers import PhoneNumberSerializer

# ✅ ML + GenAI imports
from ml_engine.predict import predict_spam
from ml_engine.explain import generate_explanation
from django.core.cache import cache
from .tasks import process_spam_score

class LookupNumberAPIView(APIView):
    def get(self, request):
        number = request.query_params.get("number")

        if not number:
            return Response({"error": "Number required"}, status=400)

        cache_key = f"phone_{number}"
        cached_data = cache.get(cache_key)

        if cached_data:
            return Response(cached_data)

        obj, _ = PhoneNumber.objects.get_or_create(number=number)

        # async processing
        process_spam_score.delay(number)

        data = PhoneNumberSerializer(obj).data

        cache.set(cache_key, data, timeout=60)

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