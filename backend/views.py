from django.shortcuts import render

from . import models

from . import serializers

from rest_framework import viewsets

class ProductView(viewsets.ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
