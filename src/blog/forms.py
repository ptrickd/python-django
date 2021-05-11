from django import forms
# from django.forms import fields
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = [
            'title',
            'content',
            'active'
        ]

class RawArticleForm(forms.Form):
    title = forms.CharField(label='',widget = forms.TextInput(attrs={'placeholder':'Your title'}))
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                'rows': 20
            }
        )
    )
    active = forms.BooleanField()