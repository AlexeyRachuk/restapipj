from django.contrib import admin
from django.forms import models

from guitars.models.guitar import Guitar, GuitarPhoto
from guitars.models.category import TypeGuitar, SubTypeGuitar, Brand, Strings, Material
from guitars.abstract.abstract import AbstractMetaModel


class GuitarPhotoAdmin(admin.StackedInline):
    model = GuitarPhoto
    extra = 0


@admin.register(Guitar)
class GuitarAdmin(admin.ModelAdmin):
    fieldsets = [
        (
            "SEO",
            {
                "fields": ["seo_title", "seo_description", "og_title", "og_description", "og_image", ]
            },
        ),
        (
            "Основное",
            {
                "fields": ["guitar_name", "guitar_article", "guitar_slug", "guitar_price", "guitar_price_old",
                           "guitar_hit", "guitar_image", "guitar_description", "guitar_date", "guitar_pub", ]
            },
        ),
        (
            "Категории",
            {
                "classes": ["wide"],
                "fields": ["guitar_type", "guitar_subtype", "guitar_brand", "guitar_string", "guitar_material", ]
            },
        ),
    ]
    list_display = ('guitar_name', 'guitar_price', 'guitar_date', 'guitar_pub')
    search_fields = ('guitar_name', 'guitar_article')
    list_editable = ('guitar_price', 'guitar_date', 'guitar_pub')
    prepopulated_fields = {'guitar_slug': ('guitar_name',)}
    inlines = [GuitarPhotoAdmin]


class SubTypeGuitarAdmin(admin.StackedInline):
    model = SubTypeGuitar
    extra = 1


@admin.register(TypeGuitar)
class TypeGuitarAdmin(admin.ModelAdmin):
    inlines = [SubTypeGuitarAdmin]


admin.site.register(Brand)
admin.site.register(Strings)
admin.site.register(Material)
