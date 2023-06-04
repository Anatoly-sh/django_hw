from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import contacts, index, ProductListView, ProductDetailView, BlogRecordListView, BlogRecordDetailView, \
    BlogRecordCreateView

app_name = CatalogConfig.name       # здесь можно: app_name = 'catalog'
# app_name = 'catalog'

urlpatterns = [
    path('', index, name='index'),
    path('index/', index, name='index'),
    path('contacts/', contacts, name='contacts'),
    # path('cards/', cards, name='cards'),
    path('product_list/', ProductListView.as_view(), name='product_list'),
    path('coin/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    # path('home/', home),
    # path('card/', card),
    path('blogrecord_list/', BlogRecordListView.as_view(), name='blog-record_list'),
    path('blogrecord_create/', BlogRecordCreateView.as_view(), name='blog-record_create'),
    path('blogrecord_detail/<int:pk>/', BlogRecordDetailView.as_view(), name='blog-record_detail'),
]
