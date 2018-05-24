from django import template
from pretix.base.i18n import LazyI18nString

register = template.Library()


@register.filter
def gdpr_localize(value):
    return str(LazyI18nString(value))
