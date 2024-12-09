from rest_framework import serializers
from rest_framework.pagination import PageNumberPagination

from .models import Portfolio,Contact

class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = ('id','image')

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

