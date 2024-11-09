from django.db import models
from django.shortcuts import render

class URL(models.Model):
    longurl = models.URLField(max_length=500)
    code = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return f"{self.code} -> {self.longurl}"
