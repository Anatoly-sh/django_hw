from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import contacts, index, ProductListView, ProductDetailView

app_name = CatalogConfig.name       # здесь можно: app_name = 'catalog'
# app_name = 'catalog'

urlpatterns = [
    path('', index, name='index'),
    # path('index/', index, name='index'),
    path('contacts/', contacts, name='contacts'),
    # path('cards/', cards, name='cards'),
    path('product_list/', ProductListView.as_view(), name='product_list'),
    path('coin/<int:pk>/', ProductDetailView.as_view(), name='coin_item'),
    # path('home/', home),
    # path('card/', card)
]
