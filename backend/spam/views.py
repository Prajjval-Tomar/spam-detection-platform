from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import PhoneNumber
from .serializers import PhoneNumberSerializer


# 🔍 Lookup API
class LookupNumberAPIView(APIView):
    def get(self, request):
        number = request.query_params.get("number")

        if not number:
            return Response({"error": "Number required"}, status=400)

        obj, created = PhoneNumber.objects.get_or_create(number=number)
        serializer = PhoneNumberSerializer(obj)

        return Response(serializer.data)


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