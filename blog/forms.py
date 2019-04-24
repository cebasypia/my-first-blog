from django import forms

from .models import Post

class PostForm(forms.ModelForm):
    document = forms.FileField(
        widget=forms.ClearableFileInput(attrs={'multiple': True}),
    )
    class Meta:
        model = Post
        fields = ('title', 'text','document')