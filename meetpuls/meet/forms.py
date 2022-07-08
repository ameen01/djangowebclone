from datetime import datetime
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit



#user forms that extend the user model filed
class UserForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()


    username = forms.CharField(max_length=100)
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=200, widget=forms.EmailInput(attrs={'placeholder':'Email',}))
    password = forms.CharField(max_length=200, widget=forms.PasswordInput(attrs={'placeholder':'Passwrod',}))
    password2 = forms.CharField(label='password',max_length=200, widget=forms.PasswordInput(attrs={'placeholder':'Conform Passwrod',}))
    age= forms.DateField(label='date of birth',widget=forms.DateInput(attrs={'tybe':'date','max': datetime.now().date()}))


# reaset password
class NewPassword(forms.Form):
    username = forms.CharField(max_length=100)

    old_password = forms.CharField(max_length=200, widget=forms.PasswordInput)
    new_password = forms.CharField(max_length=200, widget=forms.PasswordInput)
    comf_password = forms.CharField(max_length=200, widget=forms.PasswordInput)