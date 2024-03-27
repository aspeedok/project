from django import forms
from apps.posts.models.post import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["name", "text"]
