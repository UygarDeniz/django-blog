from .models import Post
from django import forms

class PostForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={
        "class" : "user-form-input",
        "placeholder" : "Title",
        "maxLength": 50
    }))
    
    content = forms.CharField(widget=forms.Textarea(attrs={
        "class": "user-form-input",
        "placeholder": "Content",
        "rows": 5
    }))
    class Meta:
        model = Post
        fields = ["title", "content"]