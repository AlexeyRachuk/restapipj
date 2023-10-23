from datetime import date

from django.db import models
from solo.models import SingletonModel
from guitars.models.category import TypeGuitar, SubTypeGuitar, Brand, Strings, Material

from guitars.abstract.abstract import AbstractMetaModel, AbstractOrderPubModel

"""Модель гитар"""


class Guitar(AbstractMetaModel, models.Model):
    guitar_name = models.CharField(
        'Название',
        max_length=150,
        db_index=True
    )
    guitar_article = models.PositiveIntegerField(
        'Артикул',
        unique=True,
    )
    guitar_slug = models.SlugField(
        'URL',
        unique=True
    )
    guitar_price = models.DecimalField(
        'Цена',
        max_digits=8,
        decimal_places=2,
    )
    guitar_price_old = models.DecimalField(
        'Старая цена',
        max_digits=8,
        decimal_places=2,
        blank=True
    )
    guitar_hit = models.BooleanField(
        'Хит',
        default=False
    )
    guitar_image = models.ImageField(
        'Изображение для превью',
        upload_to='media/'
    )
    guitar_description = models.TextField(
        'Описание',
    )
    guitar_date = models.DateField(
        'Дата добавления',
        default=date.today
    )
    guitar_pub = models.BooleanField(
        'Публикация',
        default=True
    )
    guitar_type = models.ForeignKey(
        TypeGuitar,
        verbose_name='Тип гитары',
        on_delete=models.SET_NULL,
        null=True
    )
    guitar_subtype = models.ForeignKey(
        SubTypeGuitar,
        verbose_name='Вид гитары',
        on_delete=models.SET_NULL,
        null=True
    )
    guitar_brand = models.ForeignKey(
        Brand,
        verbose_name='Бренд',
        on_delete=models.SET_NULL,
        null=True
    )
    guitar_string = models.ForeignKey(
        Strings,
        verbose_name='Струны',
        on_delete=models.SET_NULL,
        null=True
    )
    guitar_material = models.ForeignKey(
        Material,
        verbose_name='Материал',
        on_delete=models.SET_NULL,
        null=True
    )

    def __str__(self):
        return self.guitar_name

    class Meta:
        verbose_name = 'Гитара'
        verbose_name_plural = 'Гитары'
        ordering = ['-guitar_date']


"""Модель фото гитар"""


class GuitarPhoto(AbstractOrderPubModel, models.Model):
    guitar_photo = models.ImageField(
        'Фото',
        upload_to='media/'
    )
    guitar_photo_on_guitar = models.ForeignKey(
        Guitar,
        on_delete=models.SET_NULL,
        null=True,
        related_name="guitar_photo"
    )

    def __str__(self):
        return 'Фото'

    class Meta:
        verbose_name = 'Фото гитары'
        verbose_name_plural = 'Фото гитары'
        ordering = ['order']
