from django.db import models
from helpers.models import BaseModel


class ContactUs(BaseModel):
    first_name = models.CharField(max_length=128)
    subject = models.CharField(max_length=128)
    email = models.EmailField()
    message = models.TextField()
