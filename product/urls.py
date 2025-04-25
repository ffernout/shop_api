from django.urls import path
from .views import (CategoryListAPIView, CategoryDetailAPIView,
                    ProductListAPIView, ProductDetailAPIView,
                    ReviewDetailAPIView,  ReviewListAPIView)

urlpatterns = [
    path('api/v1/category/', CategoryListAPIView.as_view(), name='category-list'),
    path('category/<int:id>/', CategoryDetailAPIView.as_view(), name='category-detail'),
    path('product_list/', ProductListAPIView.as_view(), name='product-list' ),
    path('product/<int:id>/', ProductDetailAPIView.as_view(), name='product-detail' ),
    path('review_list/', ReviewListAPIView.as_view(), name='review-list' ),
    path('review_detail/', ReviewDetailAPIView.as_view(), name='review-detail' ),
]