from rest_framework import serializers
from .models import *


class BookSerializer(serializers.Serializer):
    id=serializers.IntegerField(label="Enter Book Id")
    title=serializers.CharField(label="Enter Book Title")
    author=serializers.CharField(label="Enter Author Names")

class NewsSerializer(serializers.Serializer):
    id=serializers.IntegerField(label="Enter News Id")
    title=serializers.CharField(label="Enter News Title")
    description=serializers.CharField(label="Enter description ")
    content=serializers.CharField(label="Enter content ")


class PersonSerializer(serializers.Serializer):
    id=serializers.IntegerField(label="Enter News Id")
    name=serializers.CharField(label="Enter name")
    age=serializers.CharField(label="Enter age ")
    email=serializers.CharField(label="Enter email ")
    password=serializers.CharField(label="Enter password ")