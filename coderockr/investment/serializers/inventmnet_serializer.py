from rest_framework import serializers

from ..models import Investiment


class InvestimentSerializer(serializers.ModelSerializer):
    balance = serializers.ReadOnlyField()
    investment_withdrawal = serializers.ReadOnlyField()
    class Meta:
        model = Investiment
        fields = '__all__'
