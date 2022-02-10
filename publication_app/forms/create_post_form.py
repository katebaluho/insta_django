from django import forms

from publication_app.models import Post


class CreatePostForm(forms.ModelForm):
    title = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 1}), max_length=100)
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}), max_length=300)
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    #hashtags = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}), max_length=2048)

    class Meta:
        model = Post
        fields = ['image', 'title', 'text']