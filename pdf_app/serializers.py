from rest_framework import serializers

from .models import Contact


class CreateContactSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100, min_length=1)
    contact = serializers.CharField(max_length=11, min_length=11)
    email = serializers.CharField(max_length=100)


