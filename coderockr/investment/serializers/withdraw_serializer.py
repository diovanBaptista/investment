from rest_framework import serializers

from ..models import Withdraw


class WithdrawSerializer(serializers.ModelSerializer):
    imposto = serializers.ReadOnlyField()
    valor_final = serializers.ReadOnlyField()
    value = serializers.ReadOnlyField()
    class Meta:
        model = Withdraw
        fields = '__all__'
