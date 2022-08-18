from django.contrib import admin
from django.urls import path, include
from contact.views import ContactUsView
urlpatterns = [
    path('contact', ContactUsView.as_view()),

]
