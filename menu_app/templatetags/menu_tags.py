from django import template
from ..models import Menu


register = template.Library()


@register.inclusion_tag("menu.html", takes_context=True)
def menu(context):
    menu = Menu.objects.get(menu_label='main_menu')
    return {'menu': menu.links.order_by("priority").all()}


@register.inclusion_tag("menu.html", takes_context=True)
def login_menu(context):
    if context.request.user.is_authenticated:
        menu = [
            {
                'url': "/profile/",
                'title': context.request.user.username,
            },
            {
                'url': "/logout/",
                'title': "Выйти",
            },
        ]

    else:
        menu = [
            {
                'url': "/registration/",
                'title': "Регистрация",
            },
            {
                'url': "/sigin/",
                'title': "Войти",
            },
        ]
    return {'menu': menu}