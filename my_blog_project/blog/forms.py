from django import forms
from .models import Comment, CommentorImage

# We need a form to fill comment which i declare inside the models.py

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

class CommentorImageForm(forms.ModelForm):
    class Meta:
        model = CommentorImage
        fields = ['image_commentor']
