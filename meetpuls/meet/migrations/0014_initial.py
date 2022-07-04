# Generated by Django 4.0.4 on 2022-07-04 12:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('meet', '0013_delete_profileimg'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileImg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default='avatar.png', upload_to='profiles', verbose_name='profile')),
                ('age', models.DateTimeField()),
                ('contory', models.CharField(max_length=100)),
                ('created', models.DateTimeField()),
                ('user_pic', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
