# Generated by Django 4.0.4 on 2022-06-27 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('show', '0011_rename_user_id_profileimg_user_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileimg',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
