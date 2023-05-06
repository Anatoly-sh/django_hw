from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import index, home, contacts

app_name = CatalogConfig.name       # здесь можно: app_name = 'catalog'
# app_name = 'catalog'

urlpatterns = [
    path('', index),
    path('home/', home),
    path('contacts/', contacts),
]
