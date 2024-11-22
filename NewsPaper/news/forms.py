from django import forms
from django.core.exceptions import ValidationError
from .models import Post

class PostForms(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'post_title',
            'post_author',
            'post_text',
            ]


