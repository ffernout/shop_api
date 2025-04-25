from .models import Category, Product, Review
from .serializers import ProductWithReviewsSerializer, CategorySerializer, ReviewSerializer
from rest_framework import generics
from django.db.models import Count

class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.annotate(products_count=Count('product'))
    serializer_class = CategorySerializer


class CategoryDetailAPIView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'id'


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductWithReviewsSerializer


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductWithReviewsSerializer
    lookup_field = 'id'


class ReviewListAPIView(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    lookup_field = 'id'

