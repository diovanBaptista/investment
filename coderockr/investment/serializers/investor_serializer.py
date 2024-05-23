from rest_framework import serializers
from django.contrib.auth.models import User
from ..models import Investor



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email','password']
        ref_name = "InvestmentUserSerializer"

class InvestorSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Investor
        fields = '__all__'
