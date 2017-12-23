from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Note


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(
        required=True,
        label='Username',
        max_length=32
    )
    email = forms.CharField(
        required=True,
        label='Email',
        max_length=32,
    )
    password1 = forms.CharField(
        required=True,
        label='Password',
        max_length=32,
        widget=forms.PasswordInput()
    )


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('label', 'body')
