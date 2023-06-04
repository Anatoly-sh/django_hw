from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import contacts, index, ProductListView, ProductDetailView, BlogRecordListView, BlogRecordDetailView, \
    BlogRecordCreateView, BlogRecordUpdateView, BlogRecordDeleteView, toggle_activity

app_name = CatalogConfig.name       # здесь можно: app_name = 'catalog'

urlpatterns = [
    path('', index, name='index'),
    path('index/', index, name='index'),
    path('contacts/', contacts, name='contacts'),
    path('product_list/', ProductListView.as_view(), name='product_list'),
    path('coin/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('blogrecord_list/', BlogRecordListView.as_view(), name='blog-record_list'),
    path('blogrecord_create/', BlogRecordCreateView.as_view(), name='blog-record_create'),
    path('blogrecord_apdate/<slug:slug>/', BlogRecordUpdateView.as_view(), name='blog-record_update'),
    path('blogrecord_delete/<slug:slug>/', BlogRecordDeleteView.as_view(), name='blog-record_delete'),
    path('blogrecord_detail/<slug:slug>/', BlogRecordDetailView.as_view(), name='blog-record_detail'),
    path('toggle/<slug:slug>/', toggle_activity, name='toggle_activity')
]
