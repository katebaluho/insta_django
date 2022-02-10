from django.contrib.auth.models import User

from django import forms

from account_app.models import Profile


class EditFormUser(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class EditProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    phone = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control','rows': 1}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
    github = forms.URLField(widget=forms.URLInput(attrs={'class': 'form-control', 'rows': 1}))

    class Meta:
        model = Profile
        fields = ['avatar', 'phone', 'bio', 'github']