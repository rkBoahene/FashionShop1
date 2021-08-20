from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, required=False)
    password = forms.CharField(max_length=50, required=True,widget=forms.PasswordInput())