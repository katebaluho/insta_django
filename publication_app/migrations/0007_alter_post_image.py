# Generated by Django 4.0 on 2021-12-18 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('media_app', '0001_initial'),
        ('publication_app', '0006_rename_author_post_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='media_app.media'),
            preserve_default=False,
        ),
    ]
