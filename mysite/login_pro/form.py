from django import forms


class RegisterationForm(forms.Form):
    username = forms.CharField(max_length=30)
    email = forms.EmailField()
    password = forms.CharField(max_length=20, widget=forms.PasswordInput())

class loginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=20, widget=forms.PasswordInput())