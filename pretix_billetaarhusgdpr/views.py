from django.core.urlresolvers import reverse
from pretix.base.models.event import Event
from pretix.control.views.event import (
    EventSettingsFormView, EventSettingsViewMixin,
)

from .forms import GDPRSettingsForm


class SettingsView(EventSettingsViewMixin, EventSettingsFormView):
    model = Event
    permission = 'can_change_settings'
    form_class = GDPRSettingsForm
    template_name = 'pretix_billetaarhusgdpr/settings.html'

    def get_success_url(self, **kwargs):
        return reverse('plugins:pretix_billetaarhusgdpr:settings', kwargs={
            'organizer': self.request.event.organizer.slug,
            'event': self.request.event.slug,
        })
