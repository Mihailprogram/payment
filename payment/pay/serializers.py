from rest_framework import serializers
from .models import Payment, BalanceOrganizations


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ('operation_id', 'amount', 'payer_inn', 'document_number','document_date')

class BalanceOrganizationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BalanceOrganizations
        fields = ('inn', 'balance')
