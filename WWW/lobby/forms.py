from django import forms

# Create your forms here.                                                                                                                                                                                           
class ConnectForm(forms.Form):
    username = forms.CharField(max_length=200)
    password = forms.CharField(max_length=200)
    email = forms.EmailField(max_length=200)