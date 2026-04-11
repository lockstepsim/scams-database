from django.db import models

SCAM_CHANNELS = [
    ("email", "Email"),
    ("sms", "SMS"),
    ("phone_call", "Phone call"),
    ("social_media","Social media"),
    ("in_person","In-person approach"),
    ("mail","Mail"),
    ("other","Other channel")
    ]

SCAM_TYPES = [
    ("financial", "Financial transfer scams"),
    ("identity", "Identity and impersonation scams"),
    ("investment", "Investment and wealth scams"),
    ("other", "Other scams")
    ]

class Scam(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    phishing = models.BooleanField(null=True, blank=True)
    contact_method = models.CharField(max_length=100,choices=SCAM_CHANNELS, default="undefined")
    scam_type = models.CharField(max_length=100,choices=SCAM_TYPES, default="undefined")
    date_seen = models.DateField()
    url_or_contact = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='pending')

    def __str__(self):
        return self.title