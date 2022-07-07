from django.urls import re_path as url
from pro_user.serializers import SignInSerializer
from pro_user.views import  MyTokenObtainPairView, UserRegistrationView, signin
from rest_framework_simplejwt.views import (
    
    TokenRefreshView,
)



urlpatterns = [
    url(r'^signup', UserRegistrationView.as_view()),
    url(r'^signin',MyTokenObtainPairView.as_view()),
    url(r'^refresh', TokenRefreshView.as_view(), name='token_refresh'),
    ]