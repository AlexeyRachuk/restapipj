from rest_framework import serializers

from guitars.models.guitar import Guitar, GuitarPhoto


class GuitarPhotoSerialize(serializers.ModelSerializer):
    class Meta:
        model = GuitarPhoto
        fields = '__all__'


class GuitarCatalogPageSerialize(serializers.ModelSerializer):
    guitar_type = serializers.SlugRelatedField(slug_field='type_name', read_only=True)
    guitar_subtype = serializers.SlugRelatedField(slug_field='sub_type_name', read_only=True)
    guitar_brand = serializers.SlugRelatedField(slug_field='brand_name', read_only=True)
    guitar_string = serializers.SlugRelatedField(slug_field='count_string', read_only=True)
    guitar_material = serializers.SlugRelatedField(slug_field='material_name', read_only=True)

    class Meta:
        model = Guitar
        exclude = ('guitar_date',)
