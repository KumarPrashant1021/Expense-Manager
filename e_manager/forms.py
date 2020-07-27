from django import forms
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model =  User
        fields = ['username','first_name','last_name','email','password']

        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control','type':'text','placeholder':'Username','required':True}),
            'first_name':forms.TextInput(attrs={'class':'form-control','type':'text','placeholder':'First Name','required':True}),
            'last_name':forms.TextInput(attrs={'class':'form-control','type':'text','placeholder':'Last Name','required':True}),
            'email':forms.TextInput(attrs={'class':'form-control','type':'email','placeholder':'Email','required':True}),
            'password':forms.TextInput(attrs={'class':'form-control','type':'password','placeholder':'Password','required':True}),
            }