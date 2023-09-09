from django.urls import path, include
from .views import ProductList, ProductDetail

urlpatterns = [
    path('api/', ProductList.as_view(), name='product-list'),
    path('api/<int:code>/', ProductDetail.as_view(), name='product-detail'),
]