from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
REQUIRED = 'To pole jest wymagane!'

'''
class RegisterForm(forms.Form):
    first_name = forms.CharField(required=True,
                                 error_messages={'required': REQUIRED})

    last_name = forms.CharField(required=True,
                                error_messages={'required': REQUIRED})

    login = forms.CharField(required=True,
                            error_messages={'required': REQUIRED})

    email = forms.CharField(required=True,
                            error_messages={'required': REQUIRED})

    password = forms.CharField(min_length=10, required=True,
                               error_messages={'required': REQUIRED,
                                               'min_length': 'Haslo musi składać się z min 10 znaków.'})

    password_confirmation = forms.CharField(min_length=10, required=True,
                                            error_messages={'required': REQUIRED,
                                                            'min_length': 'Haslo musi składać się z min 10 znaków.'})
'''


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