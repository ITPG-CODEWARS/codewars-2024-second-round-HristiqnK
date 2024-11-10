from django.db import models

class URL(models.Model):
    username = models.CharField(max_length=50)
    longurl = models.URLField(max_length=500)
    code = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.code} -> {self.longurl}"

    class Meta:
        unique_together = ('username', 'code')