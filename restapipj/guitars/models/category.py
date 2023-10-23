from django.db import models
from solo.models import SingletonModel

from guitars.abstract.abstract import AbstractOrderPubModel

"""Типы гитар"""


class TypeGuitar(AbstractOrderPubModel, models.Model):
    type_name = models.CharField(
        'Название типа гитары',
        max_length=80
    )
    type_url = models.SlugField(
        'URL типа',
        unique=True
    )

    def __str__(self):
        return self.type_name

    class Meta:
        verbose_name = 'Тип гитары'
        verbose_name_plural = 'Тип гитары'
        ordering = ['order']


class SubTypeGuitar(AbstractOrderPubModel, models.Model):
    sub_type_name = models.CharField(
        'Название подтипа',
        max_length=80
    )
    sub_type_url = models.SlugField(
        'URL подтипа',
        unique=True
    )
    sub_type_type = models.ForeignKey(
        TypeGuitar,
        verbose_name='Типа',
        on_delete=models.SET_NULL,
        null=True
    )

    def __str__(self):
        return self.sub_type_name

    class Meta:
        verbose_name = 'Вид гитары'
        verbose_name_plural = 'Вид гитары'
        ordering = ['order']


class Brand(AbstractOrderPubModel, models.Model):
    brand_name = models.CharField(
        'Бренд',
        max_length=80
    )
    brand_url = models.SlugField(
        'URL бренда',
        unique=True
    )

    def __str__(self):
        return self.brand_name

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренд'
        ordering = ['order']


class Strings(AbstractOrderPubModel, models.Model):
    count_string = models.PositiveSmallIntegerField(
        'Кол-во струн',
        default=0
    )

    class Meta:
        verbose_name = 'Струны'
        verbose_name_plural = 'Струны'
        ordering = ['order']


class Material(AbstractOrderPubModel, models.Model):
    material_name = models.CharField(
        'Материал',
        max_length=80
    )
    material_url = models.SlugField(
        'URL материала',
        unique=True
    )

    def __str__(self):
        return self.material_name

    class Meta:
        verbose_name = 'Материал'
        verbose_name_plural = 'Материал'
        ordering = ['order']
