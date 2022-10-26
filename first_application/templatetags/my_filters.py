from django import template

register = template.Library()

# Create custom fiter 01.
def my_filter(value, arg):
    return value + " This is a string from custom filter " + arg

register.filter('custom_filter', my_filter )



# Create custom fiter 02.
def my_filter2(value):
    return value + " This is a string from custom filter "

register.filter('custom_filter2', my_filter2 )
