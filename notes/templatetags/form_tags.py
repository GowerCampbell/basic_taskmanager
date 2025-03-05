from django import template

register = template.Library()

@register.filter
def add_class(field, css_class):
    # Ensure we're working with a BoundField
    if hasattr(field, 'as_widget'):
        return field.as_widget(attrs={"class": css_class})
    return field  # Return unchanged if not a field

@register.filter
def attr(field, attr_string):
    # Ensure we're working with a BoundField
    if hasattr(field, 'as_widget'):
        attr_name, attr_value = attr_string.split(':')
        return field.as_widget(attrs={attr_name: attr_value})
    return field  # Return unchanged if not a field

@register.filter
def add_attrs(field, attr_string):
    # Combined filter for multiple attributes (e.g., "class:form-control|rows:5")
    if not hasattr(field, 'as_widget'):
        return field
    attrs = {}
    for attr in attr_string.split('|'):
        name, value = attr.split(':')
        attrs[name] = value
    return field.as_widget(attrs=attrs)