from rest_framework import serializers
from .models import Task
from .models import CustomUser

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # Prevent password exposure

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'password')