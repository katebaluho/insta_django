# Generated by Django 4.0 on 2021-12-10 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='default.jpg', upload_to='profile_images'),
        ),
    ]
