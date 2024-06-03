from django import forms
from app.models import TODO

class signup_form(forms.Form):
    name = forms.CharField()
    password = forms.PasswordInput()


class TODOForm(forms.ModelForm):
    class Meta:
        model = TODO
        fields = ['status' ,'priority', 'title']