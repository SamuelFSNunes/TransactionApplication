from rest_framework import serializers
from api.models.modelTransaction import Transaction
from .categorySerializer import CategorySerializer
from datetime import datetime, date

class TransactionSerializer(serializers.Serializer):
    id = serializers.CharField(allow_blank=True, required=False)
    category = serializers.CharField(max_length=255)
    amount = serializers.FloatField()
    date = serializers.DateTimeField()
    description = serializers.CharField(allow_blank=True, required=False)

    def create(self, validated_data):
        return Transaction(**validated_data)

    def update(self, instance, validated_data):
        instance.category = validated_data.get('category', instance.category)
        instance.amount = validated_data.get('amount', instance.amount)
        instance.date = validated_data.get('date', instance.date)
        instance.description = validated_data.get('description', instance.description)
        return instance