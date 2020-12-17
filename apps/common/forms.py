from django import forms

class UserForm(forms.Form):
    name = forms.CharField(label="", widget=forms.TextInput(attrs={
        "class" : "form-control mt-3",
        "placeholder" : "Username here or student code",
        "id" : "username"
    }))

    password = forms.CharField(label="", widget=forms.PasswordInput(attrs= {
        "class" : "form-control mt-3",
        "placeholder" : "Password here",
        "id" : "userpassword"
    }))
