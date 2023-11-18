from django.urls import path

from api.users.api import UserApiView, user_api_view, user_detail_view

urlpatterns = [
    path('user/', UserApiView.as_view(), name="user_api"),
    path('userd/', user_api_view, name="user_api_decorator"),
    path('userd/<int:pk>', user_detail_view, name="user_detail_api")
]
