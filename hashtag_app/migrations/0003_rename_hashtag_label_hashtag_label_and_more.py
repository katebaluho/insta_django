# Generated by Django 4.0 on 2021-12-18 17:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hashtag_app', '0002_alter_hashtag_publication_alter_hashtag_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hashtag',
            old_name='hashtag_label',
            new_name='label',
        ),
        migrations.RemoveField(
            model_name='hashtag',
            name='slug',
        ),
    ]
