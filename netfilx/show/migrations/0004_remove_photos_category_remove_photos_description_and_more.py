# Generated by Django 4.0.4 on 2022-06-26 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('show', '0003_remove_profileimg_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photos',
            name='category',
        ),
        migrations.RemoveField(
            model_name='photos',
            name='description',
        ),
        migrations.RemoveField(
            model_name='photos',
            name='image',
        ),
    ]