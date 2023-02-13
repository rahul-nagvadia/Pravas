from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegistration(UserCreationForm):
    email = forms.EmailField(required=True)
    username = forms.CharField(max_length=100, required=True)
    firstname = forms.CharField(max_length=100, required=True)
    lastname = forms.CharField(max_length=100, required=True)

    class Meta:
        model = User
        fields = ("firstname", "lastname", "username",
                  "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserRegistration, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
