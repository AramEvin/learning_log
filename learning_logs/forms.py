from cProfile import label
from dataclasses import fields
from pyexpat import model
from django import forms
from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['title']
        labels = {'text': ''}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['description']
        label = {'text': 'Entry:'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
                 