from django.urls import path

from api.users.api import UserApiView

urlpatterns = [
    path('user/', UserApiView.as_view(), name="user_api")
]