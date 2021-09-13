from api import models
from django.http import JsonResponse
from django.core import serializers


def listproducts(request):

    data = serializers.serialize('json', models.Product.objects.all())

    return JsonResponse(data, safe=False)
