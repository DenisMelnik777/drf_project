from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from users.models import User




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'avatar', 'comment')