from django import forms

class user_form(forms.Form):
    #<label for="user_name">Full Name</label>
    #<input type="text" name="user_name" value="muzahid" required>
    user_name = forms.CharField()


    #<label for="user_email">User Email</label>
    #<input type="email" name="user_email" value="" required
    user_email = forms.EmailField()
