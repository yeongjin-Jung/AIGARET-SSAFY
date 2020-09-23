# from django.contrib.auth import get_user_model
from rest_framework import serializers
from accounts.models import User

# User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'name', 'age', ]