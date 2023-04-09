from django.db import models

class Sorts_of_grapes(models.Model):
    name = models.CharField('Название сорта', max_length=250)
    description = models.CharField('Описание сорта',max_length=250)
    mass = models.IntegerField('Масса грозди')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сорт винограда'
        verbose_name_plural = 'Сорта винограда'


# Create your models here.
