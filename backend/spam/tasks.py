from celery import shared_task
from .models import PhoneNumber
from ml_engine.predict import predict_spam

@shared_task
def process_spam_score(number):
    obj = PhoneNumber.objects.get(number=number)

    text = f"Message from {number}"
    score = predict_spam(text)

    obj.spam_score = score
    obj.is_spam = score > 0.5
    obj.save()