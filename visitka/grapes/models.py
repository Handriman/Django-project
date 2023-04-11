from django.db import models

class Grape(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    img_name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сорт винограда'
        verbose_name_plural = 'Сорта винограда'


# Create your models here.
