# Generated by Django 4.0 on 2021-12-20 12:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account_app', '0003_remove_profile_avatar_profile_file'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='file',
            new_name='avatar',
        ),
    ]
