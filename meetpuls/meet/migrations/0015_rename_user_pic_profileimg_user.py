# Generated by Django 4.0.4 on 2022-07-04 20:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meet', '0014_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profileimg',
            old_name='user_pic',
            new_name='user',
        ),
    ]
