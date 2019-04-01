from django import template

register = template.Library()

def div10(value):
    return value/10

register.filter('div10',div10)
