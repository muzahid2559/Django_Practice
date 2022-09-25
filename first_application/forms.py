from django import forms

class user_form(forms.Form):
    user_name = forms.CharField(required=True, label = "Full Name", widget = forms.TextInput( attrs = {'placeholder':'Enter Your Full Name', 'style':'width:300px'}))

    user_dob = forms.DateField(label = "Date of Birth", widget = forms.TextInput( attrs = {'type':'date'}))

    user_email = forms.EmailField(label = "User Email", widget = forms.TextInput( attrs = {'placeholder':'Enter Email Address', 'style':'width:300px'}))
