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
    position = models.SmallIntegerField(unique=True, verbose_name="Позиція")
    is_visible = models.BooleanField(default=True, verbose_name="Видимість")
    image = models.ImageField(upload_to=get_file_name, blank=True, verbose_name="Фото")
    desc = models.TextField(max_length=500, verbose_name="Посада", blank=True)
    image_clas = models.ImageField(upload_to=get_file_name, blank=True, verbose_name="Фото клас")

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
    position = models.SmallIntegerField(unique=True, verbose_name="Позиція")
    image = models.ImageField(upload_to=get_file_name, verbose_name="Зображення")
    is_visible = models.BooleanField(default=True, verbose_name="Видимість")
    h_1 = models.CharField(max_length=250, blank=True, verbose_name="Заголовок")
    desc = models.TextField(max_length=500, blank=True, verbose_name="Опис")
    tab_1 = models.CharField(max_length=50, verbose_name="Назва кнопки 1", blank=True)
    tab_1_url = models.URLField(blank=True, verbose_name="Посилання 1")
    tab_2 = models.CharField(max_length=50, verbose_name="Назва кнопки 1", blank=True)
    tab_2_url = models.URLField(blank=True, verbose_name="Посилання 2")

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ('position',)
        verbose_name_plural = 'Слайдер'


class About(models.Model):
    def get_file_name(self, file_name: str) -> str:
        ext = file_name.strip().split('.')[-1]
        new_file_name = f'{uuid.uuid4()}.{ext}'
        return os.path.join('about/', new_file_name)

    h1 = models.CharField(max_length=255, verbose_name="Текст заголовка")
    desc = models.TextField(max_length=1000, verbose_name="Опис")
    tab = models.CharField(max_length=55, verbose_name="Текст кнопки")
    user = models.CharField(max_length=55, verbose_name="Ім'я засновника")
    pos_user = models.CharField(max_length=55, verbose_name="Посада")
    img_user = models.ImageField(upload_to=get_file_name, verbose_name="Зображення засновника")
    is_visible = models.BooleanField(default=True, verbose_name="Видимість")
    img_1 = models.ImageField(upload_to=get_file_name, verbose_name="Зображення дитини")
    img_2 = models.ImageField(upload_to=get_file_name, verbose_name="Зображення дитини")
    img_3 = models.ImageField(upload_to=get_file_name, verbose_name="Зображення дитини")

    def __str__(self):
        return f'{self.h1}'

    class Meta:
        ordering = ('h1',)
        verbose_name_plural = 'Ми про нас'


class Testimonial(models.Model):
    def get_file_name(self, file_name: str) -> str:
        ext = file_name.strip().split('.')[-1]
        new_file_name = f'{uuid.uuid4()}.{ext}'
        return os.path.join('testimonial/', new_file_name)

    name = models.CharField(max_length=50, verbose_name="Повне ім'я")
    profession = models.TextField(max_length=50, verbose_name="Посада")
    position = models.SmallIntegerField(unique=True, verbose_name="Позиція")
    is_visible = models.BooleanField(default=True, verbose_name="Видимість")
    image = models.ImageField(upload_to=get_file_name, blank=True, verbose_name="Фото")
    desc = models.TextField(max_length=500, verbose_name="Текст", blank=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ('position',)
        verbose_name_plural = 'Відгуки'


class Classes(models.Model):
    def get_file_name(self, file_name: str) -> str:
        ext = file_name.strip().split('.')[-1]
        new_file_name = f'{uuid.uuid4()}.{ext}'
        return os.path.join('classes/', new_file_name)

    title = models.CharField(max_length=50, verbose_name="Назва")
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Ціна")
    image = models.ImageField(upload_to=get_file_name, blank=True, verbose_name="Фото")
    position = models.SmallIntegerField(unique=True, verbose_name="Позиція")
    is_visible = models.BooleanField(default=True, verbose_name="Видимість")
    teacher = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='teacher')
    age = models.CharField(max_length=50, verbose_name="Вік", default='3-5 Years')
    time = models.CharField(max_length=50, verbose_name="Час початку занять", default='9-10 AM')
    capacity = models.CharField(max_length=50, verbose_name="Кількість в групі", default='30 Kids')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ('position',)
        verbose_name_plural = 'Класи'

class Facilities(models.Model):

    h1_col_1 = models.CharField(max_length=50, verbose_name="Назва колонка №1")
    desc_col_1 = models.TextField(max_length=255, verbose_name="Опис колонка №1")
    h1_col_2 = models.CharField(max_length=50, verbose_name="Назва колонка №2")
    desc_col_2 = models.TextField(max_length=255, verbose_name="Опис колонка №2")
    h1_col_3 = models.CharField(max_length=50, verbose_name="Назва колонка №3")
    desc_col_3 = models.TextField(max_length=255, verbose_name="Опис колонка №3")
    h1_col_4 = models.CharField(max_length=50, verbose_name="Назва колонка №4")
    desc_col_4 = models.TextField(max_length=255, verbose_name="Опис колонка №4")
    position = models.SmallIntegerField(unique=True, verbose_name="Позиція")
    is_visible = models.BooleanField(default=True, verbose_name="Видимість")

    class Meta:
        ordering = ('position',)
        verbose_name_plural = 'Шкільні зручності'

class Call(models.Model):
    def get_file_name(self, file_name: str) -> str:
        ext = file_name.strip().split('.')[-1]
        new_file_name = f'{uuid.uuid4()}.{ext}'
        return os.path.join('call/', new_file_name)

    title = models.CharField(max_length=50, verbose_name="Заговок")
    desc = models.TextField(max_length=500, verbose_name="Текст", blank=True)
    image = models.ImageField(upload_to=get_file_name, blank=True, verbose_name="Зображення")
    position = models.SmallIntegerField(unique=True, verbose_name="Позиція")
    is_visible = models.BooleanField(default=True, verbose_name="Видимість")
    tab_1 = models.CharField(max_length=50, verbose_name="Текст кнопки", blank=True)
    tab_1_url = models.URLField(blank=True, verbose_name="Посилання")

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ('position',)
        verbose_name_plural = 'Заклик'

class Gallery(models.Model):
    def get_file_name(self, file_name: str) -> str:
        ext = file_name.strip().split('.')[-1]
        new_file_name = f'{uuid.uuid4()}.{ext}'
        return os.path.join('gallery/', new_file_name)

    image = models.ImageField(upload_to=get_file_name, blank=True, verbose_name="Зображення")
    position = models.SmallIntegerField(unique=True, verbose_name="Позиція")
    is_visible = models.BooleanField(default=True, verbose_name="Видимість")

    class Meta:
        ordering = ('position',)
        verbose_name = 'Фото'
        verbose_name_plural = 'Галерея'

class Contacts(models.Model):

    h1 = models.CharField(max_length=50, verbose_name="Заговок")
    address = models.CharField(max_length=50, verbose_name="Адреса")
    phone = models.CharField(max_length=50, verbose_name="Телефон")
    email = models.CharField(max_length=50, verbose_name="Пошта")
    twi_url = models.URLField(blank=True, verbose_name="Посилання на twitter")
    fb_url = models.URLField(blank=True, verbose_name="Посилання на facebook")
    youtube_url = models.URLField(blank=True, verbose_name="Посилання на youtube")
    in_url = models.URLField(blank=True, verbose_name="Посилання на LinkedIn")

    class Meta:
        ordering = ('h1',)
        verbose_name = 'Контакт'
        verbose_name_plural = 'Наші контакти'

class Appointment(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    child_name = models.CharField(max_length=50)
    child_age = models.SmallIntegerField()
    message = models.TextField(max_length=250, blank=True)

    date = models.DateField(auto_now_add=True )
    date_processing = models.DateField(auto_now=True )
    is_processed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}: {self.email}'

    class Meta:
        ordering = ('-date',)
        verbose_name_plural = 'Призначати зустріч'