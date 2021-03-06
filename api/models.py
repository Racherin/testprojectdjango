from django.db import models


class Product(models.Model):
    product_id = models.TextField()
    product_name = models.TextField()
    product_category = models.TextField()
    product_unit = models.TextField()
    product_image = models.TextField()

    class Meta:
        managed = False
        db_table = 'PRODUCT'


class ProductHistory(models.Model):
    product_id = models.TextField()
    time = models.DateTimeField()
    product_price = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'PRODUCT_HISTORY'
