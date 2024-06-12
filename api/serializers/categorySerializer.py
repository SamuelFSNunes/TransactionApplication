from rest_framework import serializers
from api.models import Category

class CategorySerializer(serializers.Serializer):
    id = serializers.CharField(allow_blank=True, required=False)
    name = serializers.CharField(max_length=255)
    description = serializers.CharField(allow_blank=True, required=False)

    def create(self, validated_data):
        return Category(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        return instance