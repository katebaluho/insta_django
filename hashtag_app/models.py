
from django.db import models

from publication_app.models import Post


class Hashtag(models.Model):
    hashtag_label = models.CharField(max_length=30)
    posts = models.ManyToManyField(Post, blank=True, related_name='hashtags')


    # @classmethod
    # def get_or_create(cls, **kwargs):
    #     request, title_form_field = kwargs['request'], kwargs['title_form_field']
    #     hashtag_text = request.POST.get(title_form_field)
    #     result_hashtag_instances = []
    #     for label in cls.hastag_labels(hashtag_text):
    #         hashtag, _ = Hashtag.objects.get_or_create(
    #             hashtag_label= '#'+label,
    #             slug=slugify(label)
    #         )
    #         result_hashtag_instances.append(hashtag)
    #     return result_hashtag_instances
    #
    # @staticmethod
    # def hastag_labels(text):
    #     hashtag_regex = r'#(\w+)'
    #     return re.findall(hashtag_regex, text)


    def __str__(self):
        return f"{self.hashtag_label}"
