# Generated by Django 4.0.4 on 2022-06-27 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('show', '0009_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileimg',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
