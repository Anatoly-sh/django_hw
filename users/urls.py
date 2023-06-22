from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import RegisterView, MyPasswordResetView, MyPasswordResetConfirmView

app_name = UsersConfig.name       # здесь можно: app_name = 'users'

# LoginView и LogoutView импортированы и не переопределены
urlpatterns = [
    path('index/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('reset_password/', MyPasswordResetView.as_view(), name='reset_password'),
    path('reset_password_sent/', MyPasswordResetView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>', MyPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', MyPasswordResetView.as_view(), name='password_reset_complete'),
]
