from guitars.models.guitar import Guitar
from django.views.generic import DetailView, ListView
from rest_framework.views import APIView
from rest_framework.response import Response
from guitars.serializers.catalog_page import GuitarCatalogPageSerialize


class CatalogPageView(APIView):

    def get(self, request):
        guitars = Guitar.objects.filter(guitar_pub=True)
        serializer = GuitarCatalogPageSerialize(guitars, many=True)
        return Response(serializer.data)
