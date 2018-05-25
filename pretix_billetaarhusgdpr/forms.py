from django.utils.translation import ugettext_lazy as _
from i18nfield.forms import I18nFormField, I18nTextarea
from pretix.base.forms import SettingsForm


class GDPRSettingsForm(SettingsForm):
    billetaarhusgdpr_message = I18nFormField(
        label=_("GDPR message"),
        help_text=_("The GDPR message will be shown before the user registers information in the system."),
        required=True,
        widget=I18nTextarea
    )

    billetaarhusgdpr_consent_text = I18nFormField(
        label=_('GDPR consent text'),
        help_text=_('The GDPR consent text must be accepted by the user before a purchase is possible.'),
        required=True,
        widget=I18nTextarea
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['billetaarhusgdpr_message'].widget.attrs['rows'] = '3'
        # self.fields['billetaarhusgdpr_message'].widget.attrs['placeholder'] = _('GDPR message placeholder')
        self.fields['billetaarhusgdpr_consent_text'].widget.attrs['rows'] = '3'
        # self.fields['billetaarhusgdpr_consent_text'].widget.attrs['placeholder'] = _('GDPR consent text placeholder')
