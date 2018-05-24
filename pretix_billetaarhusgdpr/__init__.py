from django.apps import AppConfig
from django.utils.translation import ugettext_lazy


class PluginApp(AppConfig):
    name = 'pretix_billetaarhusgdpr'
    verbose_name = 'GDPR stuff for billet.aarhus.dk'

    class PretixPluginMeta:
        name = ugettext_lazy('GDPR stuff for billet.aarhus.dk')
        author = 'Mikkel Ricky'
        description = ugettext_lazy('GDPR stuff for billet.aarhus.dk')
        visible = True
        version = '1.0.0'

    def ready(self):
        from . import signals  # NOQA


default_app_config = 'pretix_billetaarhusgdpr.PluginApp'
