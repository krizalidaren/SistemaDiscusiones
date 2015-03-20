from django.conf.urls import patterns, include, url
from apps.users.views import ExtraDataView

urlpatterns = patterns('',
    url(r'^log-out/$', 'apps.users.views.log_out', name='logout'),
    url(r'^extra-data/$', ExtraDataView.as_view(), name='extra_data'),
)
