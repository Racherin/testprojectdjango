from rest_framework.serializers import ModelSerializer
from .models import Product


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['product_id', 'product_name',
                  'product_category', 'product_unit', 'product_image']
