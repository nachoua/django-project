from django import forms
from django import Login
class UserForm(forms.ModelForm):
    class Meta:
        model = Login
        widgets = {
        'password': forms.PasswordInput(),
    }
