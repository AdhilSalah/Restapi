from django.urls import re_path as url
from pro_user.serializers import SignInSerializer
from pro_profile.views import  UserProfileView


urlpatterns = [
    url(r'profile', UserProfileView.as_view()),
    ]