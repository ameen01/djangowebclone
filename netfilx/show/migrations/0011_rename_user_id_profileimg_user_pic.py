# Generated by Django 4.0.4 on 2022-06-27 17:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('show', '0010_alter_profileimg_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profileimg',
            old_name='user_id',
            new_name='user_pic',
        ),
    ]
