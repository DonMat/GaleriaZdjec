from django import forms
from django.contrib.auth.forms import UserCreationForm
from Galeria.models import *


class RegisterForm(UserCreationForm):
    first_name = forms.TextInput()
    last_name = forms.TextInput()
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class UploadImageForm(forms.ModelForm):

    class Meta:
        model = Obrazy
        fields = ('title', 'description','date_created', 'image', 'album', 'tags')


class GallerySettingsForm(forms.ModelForm):

    class Meta:
        model = GallerySettings
        fields = ('title', 'description')


class GalleryAlbumForm(forms.ModelForm):

    class Meta:
        model = Album
        fields = ('title', 'description')