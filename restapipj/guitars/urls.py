from django.urls import path

from guitars.api.catalog_page import CatalogPageView

app_name = "guitars"

urlpatterns = [
    path(
        "api/catalog-page/",
        CatalogPageView.as_view({'get': 'list'}),
        name="api_catalog_page",
    )
]
