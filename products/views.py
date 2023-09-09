from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
from django.http import Http404
from rest_framework.pagination import PageNumberPagination


class ProductList(APIView):

    pagination_class = PageNumberPagination

    page_size = 10

    def get(self, request):
        products = Product.objects.all()

        paginator = self.pagination_class()
        result_page = paginator.paginate_queryset(products, request)

        serializers = ProductSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializers.data)
    

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductDetail(APIView):
    def get_object(self, code):
        try:
            # Modifique esta linha para buscar o produto com base no código fornecido
            return Product.objects.get(code=code)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, code):
        product = self.get_object(code)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, code):
        product = self.get_object(code)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, code):
        product = self.get_object(code)
        product.status = 'trash'
        product.save()

        return Response(status=status.HTTP_204_NO_CONTENT)
