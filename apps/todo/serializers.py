from rest_framework import serializers
from .models import Category


class CategoryListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ('id', 'name', 'created_at', 'updated_at',)

class CategoryCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ('name',)

class CategoryUpdateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ('id','name',)



class ExampleSerializer21(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    age = serializers.IntegerField()
    email = serializers.EmailField()

