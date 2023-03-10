# Generated by Django 4.1.7 on 2023-02-25 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0004_alter_headlines_options_alter_headlines_desc_classes_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='fb_url',
            field=models.URLField(blank=True, default='https://www.facebook.com/', verbose_name='Посилання на facebook'),
        ),
        migrations.AddField(
            model_name='team',
            name='in_url',
            field=models.URLField(blank=True, default='https://www.linkedin.com/', verbose_name='Посилання на LinkedIn'),
        ),
        migrations.AddField(
            model_name='team',
            name='twi_url',
            field=models.URLField(blank=True, default='https://twitter.com/', verbose_name='Посилання на twitter'),
        ),
    ]
