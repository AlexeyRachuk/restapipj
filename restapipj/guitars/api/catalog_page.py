from guitars.models.guitar import Guitar
from rest_framework import viewsets
from guitars.serializers.catalog_page import GuitarCatalogPageSerialize


class CatalogPageView(viewsets.ModelViewSet):
    queryset = Guitar.objects.filter(guitar_pub=True)
    serializer_class = GuitarCatalogPageSerialize
