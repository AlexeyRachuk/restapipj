from django.contrib import admin

from guitars.models.guitar import Guitar, GuitarPhoto, GuitarCategory
from guitars.models.category import TypeGuitar, SubTypeGuitar, Brand, Strings, Material


class GuitarCategoryAdmin(admin.StackedInline):
    model = GuitarCategory
    extra = 1


class GuitarPhotoAdmin(admin.StackedInline):
    model = GuitarPhoto
    extra = 1


@admin.register(Guitar)
class GuitarAdmin(admin.ModelAdmin):
    list_display = ('guitar_name', 'guitar_price', 'guitar_date', 'guitar_pub')
    search_fields = ('guitar_name', 'guitar_article')
    list_editable = ('guitar_price', 'guitar_date', 'guitar_pub')
    prepopulated_fields = {'guitar_slug': ('guitar_name',)}
    inlines = [GuitarCategoryAdmin, GuitarPhotoAdmin]


class SubTypeGuitarAdmin(admin.StackedInline):
    model = SubTypeGuitar
    extra = 1


@admin.register(TypeGuitar)
class TypeGuitarAdmin(admin.ModelAdmin):
    inlines = [SubTypeGuitarAdmin]


admin.site.register(Brand)
admin.site.register(Strings)
admin.site.register(Material)
