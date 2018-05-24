from django.core.urlresolvers import resolve, reverse
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _
from pretix.base.i18n import LazyI18nString
from pretix.control.signals import nav_event_settings
from pretix.presale.signals import checkout_confirm_messages


@receiver(nav_event_settings, dispatch_uid="billetaarhusgdpr_nav_event_settings")
def nav_event_settings(sender, request=None, **kwargs):
    # @see https://docs.pretix.eu/en/latest/development/api/general.html#pretix.control.signals.nav_event_settings
    url = resolve(request.path_info)
    if not request.user.has_event_permission(request.organizer, request.event, 'can_change_event_settings', request=request):
        return []
    else:
        return [
            {
                'label': _('GDPR'),
                'url': reverse('plugins:pretix_billetaarhusgdpr:settings', kwargs={
                    'event': request.event.slug,
                    'organizer': request.event.organizer.slug
                }),
                'active': (url.namespace == 'plugins:pretix_billetaarhusgdpr'),
                'icon': 'bar-chart',
            }
        ]


@receiver(checkout_confirm_messages, dispatch_uid="billetaarhusgdpr_confirm_messages")
def confirm_messages(sender, *args, **kwargs):
    # @see https://docs.pretix.eu/en/latest/development/api/general.html#pretix.presale.signals.checkout_confirm_messages
    return {
        # @FIXME: We shouldn't have to use LazyI18nString here!
        'gdpr': str(LazyI18nString(sender.settings.billetaarhusgdpr_consent_text))
    }
