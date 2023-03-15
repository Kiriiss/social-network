from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from users.models import AbstrapUser


class AbstrapUserCreationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    photo = forms.FileField(widget=forms.FileInput(attrs={'class': 'file-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg'}))

    class Meta:
        model = AbstrapUser
        fields = ('username', 'email', 'password1', 'password2', 'photo')


class AbstrapAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg'}))

    class Meta:
        model = AbstrapUser
        fields = ('username', 'password')


class EditProfileForm(UserChangeForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    photo = forms.FileField(widget=forms.FileInput(attrs={'class': 'file-control'}))

    class Meta:
        model = AbstrapUser
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'photo'
        )
