from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend


class ModelBaseViewSet(ModelViewSet):
    filter_backends = [DjangoFilterBackend]
    pagination_class = PageNumberPagination
