from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


from .forms import SubjectForm
from .models import Subject

from apps.teachers.models import Teacher

# Create your views here.
def list_all_subjects(request):
    subjects = Subject.objects.all()
    return render(request, "subjects/all_subjects.html", {
        "subjects" : subjects
    })

def subject_form(request):
    return render(request, "subjects/create_subject.html", {
        "form" : SubjectForm()
    })

def create_subject(request):
    if request.method == "POST":
        form = SubjectForm(request.POST)

        teacher= Teacher.objects.get(id=request.POST['teacher'])

        subject = Subject(name=request.POST['name'], schedule=request.POST['schedule'], 
                        capacity=request.POST['capacity'], description=request.POST['description'], teacher=teacher) 
        subject.save()
        
        return render(request, "subjects/create_subject.html", {
            "msg" : "Created successfully",
            "success"  : True,
            "form" : SubjectForm()
        })

    else:
        return render(request, "subjects/create_subject.html", {
            "msg" : "An error ocurred during the process",
            "success" : False,
            "form" : SubjectForm(request.POST)
        })


def delete_subject(request, id):
    Subject.objects.get(id=id).delete()
    return HttpResponseRedirect(reverse('list-all-subjects'))


def update_form(request, id):
    subject = Subject.objects.get(id=id)
    form = SubjectForm()

    form.initial = {
        "name" : subject.name,
        "schedule" : subject.schedule,
        "capacity" : subject.capacity,
        "teacher" : subject.teacher,
        "description" : subject.description
    }

    return render(request, "subjects/update_subject.html", {
        "form" : form,
        "subject_id" : subject.id
    })

def update_subject(request, id):
    form = SubjectForm(request.POST)
    subject = Subject.objects.get(id=id)

    if request.method == "POST":
        subject.name = request.POST['name']
        subject.schedule = request.POST['schedule']
        subject.capacity = request.POST['capacity']
        subject.description = request.POST['description']


        subject.teacher = Teacher.objects.get(id=request.POST['teacher']) 

        subject.save()

        return render(request, "subjects/update_subject.html", {
            "form" : form,
            "success" : True,
            "msg" : "Updated successfully",
            "subject_id" : subject.id
        })
    
    else:
        return render(request, "subjects/update_subject.html", {
            "form" : form,
            "success" : False,
            "msg" : "An error ocurred during the process",
            "subject_id" : subject.id
        })

def get_subjects_count():
    return Subject.objects.all().count()

def update_subject_capacity(id):
    subject = Subject.objects.get(id=id)
    if subject.capacity > 0:
        subject.capacity -= 1
    subject.save()