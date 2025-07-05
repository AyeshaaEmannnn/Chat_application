from rest_framework import serializers
from .models import *

class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model=Signup
        fields='__all__'
        
class LoginSerializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField()
    
    def validate(self,data):
        username=data.get('username')
        password=data.get('password')
        
        try:
            user=Signup.objects.get(username=username)
        except Signup.DoesNotExist:
            raise serializers.ValidationError('Incorrect username')
        if user.password!=password:
            raise serializers.ValidationError('Incorrect Password')
        
        data['user']=user
        return data

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ['id', 'sender', 'receiver', 'message', 'timestamp']
        
        