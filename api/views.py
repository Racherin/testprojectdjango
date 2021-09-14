from .models import Product
from .serialzers import ProductSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class ProductList(APIView):

    def get(self, request, format=None):
        all_products = Product.objects.all()
        serializer = ProductSerializer(all_products, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        pass

    def put(self, request, format=None):
        pass

    def delete(self, request, format=None):
        pass
