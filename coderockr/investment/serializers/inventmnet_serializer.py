from rest_framework import serializers

from ..models import Investiment


class InvestimentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Investiment
        fields = '__all__'
