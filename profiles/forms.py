from django import forms
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
    def __init__(self, *args, **kwargs):
        super(UserForm,self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs.update({'class':'form-control','placeholder':'Username'})
        self.fields['email'].widget.attrs.update({'class':'form-control','placeholder':'Email'})
        self.fields['password'].widget.attrs.update({'class':'form-control','placeholder':'Password'})
