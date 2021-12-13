from django.db import migrations, models


def create_users_to_post(apps, schemas_editor):
    user_model = apps.get_model('auth', "User")
    first_author = user_model.objects.all().first()
    post_model = apps.get_model('publication_app', "Post")
    posts = post_model.objects.filter(author__isnull=True).all()
    for post in posts:
        publication = post_model(author=first_author)
        publication.save()


class Migration(migrations.Migration):
    dependencies = [
        ('publication_app', '0003_alter_post_author'),
    ]

    operations = [
        migrations.RunPython(create_users_to_post),
    ]