# Generated by Django 4.0.4 on 2022-06-27 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('show', '0007_pro_prof_delete_profileimg'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pro',
            name='user_id',
        ),
        migrations.DeleteModel(
            name='Prof',
        ),
        migrations.DeleteModel(
            name='Pro',
        ),
    ]
