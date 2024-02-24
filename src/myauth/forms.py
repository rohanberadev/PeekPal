from django import forms

class CreateUserForm (forms.Form):
    username = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=255)
    password1 = forms.CharField(min_length=8)
    password2 = forms.CharField(min_length=8)


class LoginUserForm (forms.Form):
    username_or_email = forms.CharField(max_length=255)
    password = forms.CharField(min_length=8)