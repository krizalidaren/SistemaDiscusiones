from django.shortcuts import render
from django.views.generic import ListView
from apps.discuss.models import Question, Tag


class QuestionListView(ListView):
    model = Question
    context_object_name = 'questions'

    def get_context_data(self, **kwargs):
        context = super(QuestionListView, self).get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context
