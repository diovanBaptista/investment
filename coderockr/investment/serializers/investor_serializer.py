from rest_framework import serializers
from django.contrib.auth.models import User
from ..models import Investor
from django.views.decorators.csrf import csrf_exempt

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password',]
        ref_name = "InvestmentUserSerializer"
        # extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        
        password = validated_data.get('password')
        if password:
            instance.set_password(password)
        
        instance.save()
        return instance

class InvestorSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    data_criacao = serializers.ReadOnlyField()
    class Meta:
        model = Investor
        fields = '__all__'
    @csrf_exempt
    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user = user_serializer.save()
            investor = Investor.objects.create(user=user, **validated_data)
            return investor
        else:
            raise serializers.ValidationError(user_serializer.errors)
        
    @csrf_exempt  
    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', None)
        if user_data:
            user_serializer = UserSerializer(instance.user, data=user_data, partial=True)
            if user_serializer.is_valid(raise_exception=True):
                user_serializer.save()
        instance.name = validated_data.get('name', instance.name)
        instance.cpf = validated_data.get('cpf', instance.cpf)
        instance.save()
        return instance
