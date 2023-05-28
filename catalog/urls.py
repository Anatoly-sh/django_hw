from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import index, contacts, card, coin

app_name = CatalogConfig.name       # здесь можно: app_name = 'catalog'
# app_name = 'catalog'

urlpatterns = [
    path('', index, name='index'),
    # path('index/', index, name='index'),
    path('contacts/', contacts, name='contacts'),
    # path('cards/', cards, name='cards'),
    path('product_rew/', card, name='product_rew'),
    path('coin/<int:pk>/', coin, name='coin_item'),
    # path('home/', home),
    # path('card/', card)
]
