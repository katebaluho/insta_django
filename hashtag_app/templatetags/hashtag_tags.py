from django import template
from ..models import Hashtag


register = template.Library()

#TODO: нужно или нет??
@register.inclusion_tag("hashtags_block.html", takes_context=True)
def hashtags_in_post(context, post):
    itm = Hashtag.objects.filter(publication = post).all()
    print("post have",itm)
    return {'hashtags_in_post': itm}