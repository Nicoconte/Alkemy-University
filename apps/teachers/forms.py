from django import forms

class TeacherForm(forms.Form):
    name = forms.CharField(label="", widget=forms.TextInput(attrs = {
        "class" : "form-control mt-3",
        "placeholder" : "Name" 
    }))

    dni = forms.CharField(label="", widget=forms.TextInput(attrs = {
        "class" : "form-control mt-3", 
        "placeholder" : "DNI"
    }))
    