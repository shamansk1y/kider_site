# Generated by Django 4.1.7 on 2023-02-25 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0002_schedule'),
    ]

    operations = [
        migrations.CreateModel(
            name='Headlines',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_facilities', models.CharField(max_length=50, verbose_name='Заговок')),
                ('desc_facilities', models.TextField(blank=True, max_length=500, verbose_name='Текст')),
                ('title_classes', models.CharField(max_length=50, verbose_name='Заговок')),
                ('desc_classes', models.TextField(blank=True, max_length=500, verbose_name='Текст')),
                ('title_teachers', models.CharField(max_length=50, verbose_name='Заговок')),
                ('desc_teachers', models.TextField(blank=True, max_length=500, verbose_name='Текст')),
                ('title_testimonial', models.CharField(max_length=50, verbose_name='Заговок')),
                ('desc_testimonial', models.TextField(blank=True, max_length=500, verbose_name='Текст')),
            ],
        ),
    ]
