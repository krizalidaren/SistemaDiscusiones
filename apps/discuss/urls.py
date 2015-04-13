from django.conf.urls import patterns, include, url
from apps.discuss.views import QuestionListView, QuestionCreateView
from apps.home.views import IndexView

urlpatterns = patterns('',
    url(r'^preguntas/$', QuestionListView.as_view(), name='questions'),
    url(r'^preguntar/$', QuestionCreateView.as_view(), name='create_question'),
    url(r'^buscar-ajax/$', 'apps.discuss.views.BuscarAjax', name='buscar'),
)
