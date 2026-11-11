from django import forms
from django.contrib.auth.models import User
from .models import UserDetails
from django_recaptcha.fields import ReCaptchaField
from .models import vendorRegistration




class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['username','email','password']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserDetails
        fields = ['age','phone','house_no','landmark','street','city','state','zipcode','userimg']
    captcha = ReCaptchaField()

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model =User
        fields = ['username','email']

class UserProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserDetails
        fields = ['age','phone','house_no','landmark','street','city','state','zipcode','userimg']




class VendorRegistrationForm(forms.ModelForm):
    class Meta:
        model = vendorRegistration
        exclude = ['user', 'is_approved']
