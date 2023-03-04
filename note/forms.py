from django import forms
from .models import Note

class NoteForm(forms.ModelForm):
    topic=forms.CharField(max_length=100, required=True, help_text="Enter Note's Topic e.g A Day In San Francisco")
    entry=forms.Textarea(attrs={'cols': 100})

    class Meta:
        model= Note
        fields = ['topic', 'entry', 'status']

class SearchForm(forms.Form):
    topic = forms.CharField(max_length=200, help_text="Enter The Note's Topic Accurately")