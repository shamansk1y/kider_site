from django.db import models
import os
import uuid

class Team(models.Model):

    def get_file_name(self, file_name: str) -> str:
        ext = file_name.strip().split('.')[-1]
        new_file_name = f'{uuid.uuid4()}.{ext}'
        return os.path.join('team/', new_file_name)

    name = models.CharField(max_length=50, verbose_name="Повне ім'я")
    profession = models.TextField(max_length=50, verbose_name="Посада")
    position = models.SmallIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)
    image = models.ImageField(upload_to=get_file_name, blank=True, verbose_name="Фото")
    desc = models.TextField(max_length=500, verbose_name="Посада", blank=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ('position',)
        verbose_name_plural = 'Наша команда'


class Slider(models.Model):

    def get_file_name(self, file_name: str) -> str:
        ext = file_name.strip().split('.')[-1]
        new_file_name = f'{uuid.uuid4()}.{ext}'
        return os.path.join('slider/', new_file_name)


    title = models.CharField(max_length=50, verbose_name="Назва слайду")
    position = models.SmallIntegerField(unique=True)
    image = models.ImageField(upload_to=get_file_name, verbose_name="Зображення")
    is_visible = models.BooleanField(default=True)
    h_1 = models.CharField(max_length=250, blank=True)
    desc = models.TextField(max_length=500, blank=True)
    tab_1 = models.CharField(max_length=50, verbose_name="Назва кнопки 1", blank=True)
    tab_1_url = models.URLField(blank=True)
    tab_2 = models.CharField(max_length=50, verbose_name="Назва кнопки 1", blank=True)
    tab_2_url = models.URLField(blank=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ('position',)
        verbose_name_plural = 'Слайдер'

