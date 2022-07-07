from rest_framework import serializers
from .models import UserProfile
class UserProfileSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = UserProfile
        fields = ('first_name','last_name','phone_number','age','gender')