from rest_framework import serializers
from pro_profile.models import UserProfile
from .models import  User
from django.contrib.auth import authenticate, login
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.settings import api_settings



class UserSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = UserProfile
        fields = ('first_name','last_name','phone_number','age','gender')
        


class UserRegistrationSerializer(serializers.ModelSerializer):

    profile = UserSerializer(required = False)

    class Meta:
        model = User
        fields = ('email','password','profile')
        extra_kwargs = {'password':{'write_only':True}}

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user = User.objects.create_user(**validated_data)
        UserProfile.objects.create(
            user=user,
            first_name = profile_data['first_name'],
            last_name = profile_data['last_name'],
            phone_number = profile_data['phone_number'],
            gender = profile_data['gender'],
            age = profile_data['age'],

        )

        return user










class SignInSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255, required=True)
    password = serializers.CharField(max_length=255, required=True, write_only=True)


from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        
        # ...

        return token    

