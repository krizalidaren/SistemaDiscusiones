from django import forms
from apps.discuss.models import Question


class CreateQuestionForm(forms.ModelForm):

    title = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Titulo'
    }))

    description = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Contenido',
        'rows': 4
    }))

    class Meta:
        model = Question
