from rest_framework import serializers

from .models import Transactions


class TransactionsSerializer(serializers.Serializer):
    transaction_id = serializers.CharField()
    transaction_date = serializers.CharField()
    transaction_amount = serializers.CharField()
    client_id = serializers.CharField()
    client_name = serializers.CharField()
