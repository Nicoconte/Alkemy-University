from django import forms

from apps.teachers.models import Teacher

def get_all_teachers():
    return Teacher.objects.all()

class SubjectForm(forms.Form):
    name = forms.CharField(label="", widget=forms.TextInput(attrs = {
        "class" : "form-control mt-3",
        "placeholder" : "Name"
    }))

    schedule = forms.TimeField(label="", input_formats='%H:%M:%S', widget=forms.TimeInput(attrs={
        "class" : "form-control mt-3",
        "placeholder" : "Schedule"
    }))

    capacity = forms.IntegerField(label="", widget=forms.TextInput(attrs= {
        "class" : "form-control mt-3",
        "placeholder" : "Capacity"
    }))

    teacher = forms.ModelChoiceField(label="", queryset=Teacher.objects.filter(is_active=True), initial=0, widget=forms.Select(attrs={
        "class" : "form-control mt-3"
    }))

    description = forms.CharField(label="", widget=forms.Textarea(attrs = {
        "class" : "form-control mt-3",
        "placeholder" : "Description about the subject"
    }))
