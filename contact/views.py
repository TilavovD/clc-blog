from django.shortcuts import render
from rest_framework import generics
# Create your views here.
from .models import ContactUs
from .serializer import ContactSerializer

class ContactUsView(generics.CreateAPIView):
    queryset = ContactUs.objects.all()
    serializer_class = ContactSerializer