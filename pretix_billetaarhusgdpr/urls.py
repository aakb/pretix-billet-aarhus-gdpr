from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^control/event/(?P<organizer>[^/]+)/(?P<event>[^/]+)/billetaarhusgdpr/settings',
        views.SettingsView.as_view(), name='settings'),
]
