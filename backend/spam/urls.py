from django.urls import path
from .views import LookupNumberAPIView, ReportSpamAPIView

urlpatterns = [
    path("lookup/", LookupNumberAPIView.as_view()),
    path("report/", ReportSpamAPIView.as_view()),
]