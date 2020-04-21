from django import forms
from . import models
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = [
            'post',
            'name',
            'email',
            'text',
        ]
        labels = {
            'text': 'Comment'
        }
        widgets = {
            'post': forms.HiddenInput()
        }
class CommentlikeForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = [
            'likes',
            'dislikes',
        ]
        labels = {
            'like': 'likes'
        }
