from django.contrib.auth.views import LoginView
from django.urls import path

from users.apps import UsersConfig

app_name = UsersConfig.name       # здесь можно: app_name = 'users'


urlpatterns = [
    path('index/', LoginView.as_view(), name='login'),
]
