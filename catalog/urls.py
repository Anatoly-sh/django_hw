from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import index, home, contacts, card, coin, cards

app_name = CatalogConfig.name       # здесь можно: app_name = 'catalog'
# app_name = 'catalog'

urlpatterns = [
    path('index/', index, name='index'),
    path('home/', home),
    path('contacts/', contacts),
    path('card/', card),
    path('cards/', cards),
    path('coin/<int:pk>/', coin, name='coin_item')
]
