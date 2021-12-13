from django import template
from ..models import Hashtag


register = template.Library()

#TODO: нужно или нет??
@register.inclusion_tag("hashtags_block.html", takes_context=True)
def hashtags_in_post(context, post):
    hashtags = Hashtag.objects.filter(publication = post).all()
    text = post.text
    template = '<a href="{itm.slug}">{itm.hashtag_label}</a>'
    for itm in hashtags:
        print('itm.hashtag_label',itm.hashtag_label)
        text = text.replace(itm.hashtag_label, template.format(itm = itm))
    return {'hashtags_in_post': text}