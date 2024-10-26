from django.urls import path
from .views import RegisterAPI, LoginAPI, LogoutAPI, PasswordResetRequestAPI, PasswordResetConfirmAPI

urlpatterns = [
    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('logout/', LogoutAPI.as_view(), name='logout'),
    path('password-reset/', PasswordResetRequestAPI.as_view(), name='password-reset-request'),
    path('reset-password/<uidb64>/<token>/', PasswordResetConfirmAPI.as_view(), name='password-reset-confirm'),
]
