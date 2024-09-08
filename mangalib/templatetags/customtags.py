from django import template

register = template.Library()

@register.simple_tag
def hello_world(username):
    return f"Hi {username} !"