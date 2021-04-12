from django.db import models
from autoslug import AutoSlugField


class YazilarModel(models.Model):
    baslik = models.CharField(max_length='50')
    icerik = models.TextField()
    olusturulma_tarihi = models.DateTimeField(auto_now_add=True)
    duzenlenme_tarihi = models.DateTimeField(auto_now_add=True)
    slug = AutoSlugField(populate_from='baslik', unique=True)
