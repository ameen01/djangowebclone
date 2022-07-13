from datetime import datetime
from django import forms
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Post ,ProfileImg

#
class PostForm(forms.ModelForm):
    class meta:
        model = Post
        fields = ['caption','image']
       




#user forms that extend the user model filed
YEARS= [x for x in range(1940,2023)]
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
    # age= forms.DateField(label='date of birth',widget=forms.SelectDateWidget(years=YEARS))

#log the user in
class UserIN(forms.Form):
    username = forms.CharField(max_length=100,)
    password = forms.CharField(max_length=200, widget=forms.PasswordInput(attrs={'placeholder':'Passwrod',}))




# reaset password
class NewPassword(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=200, widget=forms.EmailInput(attrs={'placeholder':'Email',}))
    old_password = forms.CharField(max_length=200, widget=forms.PasswordInput)
    new_password = forms.CharField(max_length=200, widget=forms.PasswordInput)
    comf_password = forms.CharField(max_length=200, widget=forms.PasswordInput)

class EdUser(forms.ModelForm):
    class Mata:
        model = Post


class ProfileImgForm(forms.ModelForm):
    class Mata:
        model = ProfileImg
        fields = "__all__" # will render every fields that in models
        exclude = ['title'] # any fields name in the list will not ber render