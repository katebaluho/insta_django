from django.contrib.auth.models import User

from django.forms import ModelForm

class RegistrationForm(ModelForm):
    class Meta:
        model = User
        fields = ("username", "email", "password")


    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
            # Так делать не надо
            # profile = Profile(user=user)
            # profile.save()
        return user