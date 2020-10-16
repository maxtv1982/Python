from django import template

register = template.Library()


@register.filter
def choose_color(number):
    color = ''
    if number:
        if float(number) < 0:
            color = 'green'
        elif 1 < float(number) <= 2:
            color = 'LightCoral'
        elif 2 < float(number) <= 5:
            color = 'Red'
        elif float(number) > 5:
            color = 'DarkRed'
    return color


@register.filter
def cut_list(lists):
    return lists.pop(0)
