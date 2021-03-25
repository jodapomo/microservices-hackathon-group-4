from django.urls import path
from apps.users.api import UserAPIView, UserDetailAPIView

urlpatterns = [
    path('', UserAPIView.as_view(), name='users_api'),
    path('<str:pk>/', UserDetailAPIView.as_view(), name='detail_user_api')
]