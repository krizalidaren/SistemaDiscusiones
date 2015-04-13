from django.core import serializers
from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.views.generic import ListView, CreateView
from apps.discuss.forms import CreateQuestionForm
from apps.discuss.models import Question, Tag

from braces.views import LoginRequiredMixin


class QuestionListView(ListView):
    model = Question
    context_object_name = 'questions'

    def get_context_data(self, **kwargs):
        context = super(QuestionListView, self).get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context


class QuestionCreateView(LoginRequiredMixin, CreateView):
    model = Question
    form_class = CreateQuestionForm
    success_url = '/'
    login_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        super(QuestionCreateView, self).form_valid(form)

    def form_invalid(self, form):
        super(QuestionCreateView, self).form_invalid(form)


def BuscarAjax(request):
    if request.is_ajax():
        tag = Tag.objects.get(id=request.GET['id'])
        questions = Question.objects.filter(tag=tag)
        data = serializers.serialize('json', questions, fields={'title', 'description', 'modified'})
        return HttpResponse(data, content_type='application/json')
    else:
        raise Http404
