from django.shortcuts import render
from rest_framework import generics
# Create your views here.
from .serializers import *
from .models import *

class PortfolioCreateListView(generics.ListCreateAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer

class ContactCreateListView(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

