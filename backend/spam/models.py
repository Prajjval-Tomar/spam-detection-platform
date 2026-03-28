from django.db import models

class PhoneNumber(models.Model):
    number = models.CharField(max_length=15, unique=True)
    
    # Spam related fields
    is_spam = models.BooleanField(default=False)
    spam_score = models.FloatField(default=0.0)
    reports = models.IntegerField(default=0)

    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.number
    class Meta:
        db_table = "phone_numbers"
        ordering = ["-created_at"]