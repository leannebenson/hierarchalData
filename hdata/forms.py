from django import forms
from .models import File
from mptt.forms import TreeNodeChoiceField

class CreateFileForm(forms.Form):
    name = forms.CharField(max_length=100)
    parent = TreeNodeChoiceField(queryset=File.objects.all())

class LoginForm(forms.Form):
    username = forms.CharField(max_length=240)
    password = forms.CharField(widget=forms.PasswordInput)