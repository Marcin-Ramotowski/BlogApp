from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Post, CATEGORY


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(label="Imię:", max_length=20)
    last_name = forms.CharField(label="Nazwisko:", max_length=20)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')


class PostForm(forms.ModelForm):
    category = forms.ChoiceField(label="Kategoria:", choices=CATEGORY)
    title = forms.CharField(label="Tytuł:")
    content = forms.CharField(label="Treść:", widget=forms.Textarea)

    class Meta:
        model = Post
        fields = ('category', 'title', 'content')
