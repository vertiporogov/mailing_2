from django.contrib.auth.views import PasswordResetView
from django.urls import path, reverse_lazy

from users.apps import UsersConfig
from users.views import LoginView, LogoutView, RegisterView, confirm_email, UserProfileView, generate_new_password

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('validate/<token>/', confirm_email, name='validate'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('profile/password/', generate_new_password, name='generate_new_password'),
    path('password-reset/',
         PasswordResetView.as_view(template_name='users/password_reset_form.html'),
         name='password_reset'),
]
