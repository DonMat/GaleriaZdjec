from django import forms

REQUIRED = 'To pole jest wymagane!'


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
