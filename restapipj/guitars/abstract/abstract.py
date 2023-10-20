from django.db import models


class AbstractMetaModel(models.Model):
    seo_title = models.CharField('SEO title', max_length=120, blank=True, null=True)
    seo_description = models.CharField('SEO description', max_length=255, blank=True, null=True)
    og_title = models.CharField('OG title', max_length=120, blank=True, null=True)
    og_description = models.CharField('OG description', max_length=255, blank=True, null=True)
    og_image = models.ImageField('OG image', upload_to='images/', blank=True, null=True)

    class Meta:
        abstract = True


class AbstractOrderPubModel(models.Model):
    order = models.PositiveSmallIntegerField(
        'Порядок',
        default=0
    )
    pub = models.BooleanField(
        'Публикация',
        default=True
    )

    class Meta:
        abstract = True
