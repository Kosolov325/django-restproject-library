from dataclasses import fields
from rest_framework import serializers
from api.models import *

class LivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livro
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["pk", "username", "password", "livros"]
    
    def to_representation(self, instance):  
        data = super().to_representation(instance)
        data['livros'] = LivroSerializer(instance.livros.all(), many=True).data
        return data 
               


        