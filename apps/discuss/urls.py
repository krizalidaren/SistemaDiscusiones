from django.conf.urls import patterns, include, url
from apps.discuss.views import QuestionListView
from apps.home.views import IndexView

urlpatterns = patterns('',
    url(r'^preguntas/$', QuestionListView.as_view(), name='questions'),
)
