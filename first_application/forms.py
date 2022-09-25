from django import forms

class user_form(forms.Form):
    #<label for="user_name">Full Name</label>
    #<input type="text" name="user_name" value="" placeholder="Enter Your FUll Name" style="width:300px" required>
    user_name = forms.CharField(required=True, label = "Full Name", widget = forms.TextInput( attrs = {'placeholder':'Enter Your Full Name', 'style':'width:300px'}))


    #<input type="date">
    user_dob = forms.DateField(label = "Date of Birth", widget = forms.TextInput( attrs = {'type':'date'}))


    #<label for="user_email">User Email</label>
    #<input type="email" name="user_email" value="" required>
    user_email = forms.EmailField(label = "User Email")
