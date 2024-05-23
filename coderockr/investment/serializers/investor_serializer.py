from rest_framework import serializers
from django.contrib.auth.models import User
from ..models import Investor


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password',]
        ref_name = "InvestmentUserSerializer"
        # extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class InvestorSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    data_criacao = serializers.ReadOnlyField()
    class Meta:
        model = Investor
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user = user_serializer.save()
            investor = Investor.objects.create(user=user, **validated_data)
            return investor
        else:
            raise serializers.ValidationError(user_serializer.errors)
