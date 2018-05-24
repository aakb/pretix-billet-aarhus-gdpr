from django.utils.translation import ugettext_lazy as _
from i18nfield.forms import I18nFormField, I18nTextarea
from pretix.base.forms import SettingsForm


class GDPRSettingsForm(SettingsForm):
    billetaarhusgdpr_message = I18nFormField(
        label=_("GDRP message"),
        help_text=_("GDPR 87."),
        required=True,
        widget=I18nTextarea
    )

    billetaarhusgdpr_consent_text = I18nFormField(
        label=_('GDPR consent text'),
        help_text=_('This text needs to be confirmed by the user before a purchase is possible. You could for example '
                    'link your terms of service here. If you use the Pages feature to publish your terms of service, '
                    'you don\'t need this setting since you can configure it there.'),
        required=True,
        widget=I18nTextarea
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['billetaarhusgdpr_message'].widget.attrs['rows'] = '3'
        # self.fields['billetaarhusgdpr_message'].widget.attrs['placeholder'] = _(
        #     'e.g. I hereby confirm that I have read and agree with the event organizer\'s terms of service '
        #     'and agree with them.'
        # )
        self.fields['billetaarhusgdpr_consent_text'].widget.attrs['rows'] = '3'
        # self.fields['billetaarhusgdpr_consent_text'].widget.attrs['placeholder'] = _(
        #     'e.g. I hereby confirm that I have read and agree with the event organizer\'s terms of service '
        #     'and agree with them.'
        # )
