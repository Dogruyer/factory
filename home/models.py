from django.db import models


class Maliyet(models.Model):
    sipno = models.CharField(max_length=100)
    hammadde_maliyet = models.CharField(max_length=100, default="0")
    zaman_maliyet = models.CharField(max_length=100, default="0")
    makine_maliyet = models.CharField(max_length=100, default="0")
    malzeme_maliyet = models.CharField(max_length=100, default="0")