from django import forms

# Create your forms here.                                                                                                                                                                                           
class ConnectForm(forms.Form):
    username = forms.CharField(max_length=200)
    password = forms.CharField(widget=forms.PasswordInput())
    email = forms.EmailField(max_length=200)