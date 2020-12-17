from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import TeacherForm

from .models import Teacher

# Create your views here.
def teacher_form(request):
    return render(request, "teachers/create_teacher.html", {
        "form" : TeacherForm
    })

def create_teacher(request):
    #TODO: refactor! Validate role and token
    if request.method == "POST":
        form = TeacherForm(request.POST)

        teacher = Teacher(name=request.POST['name'], dni=request.POST['dni'], is_active=True)
        teacher.save()

        return render(request, "teachers/create_teacher.html", {
            "msg" : "Created successfully",
            "success"  : True,
            "form" : TeacherForm()
        })
    else:
        return render(request, "teachers/create_teacher.html", {
            "msg" : "An error ocurred during the process",
            "success" : False,
            "form" : TeacherForm(request.POST)
        })

def teacher_form_update(request, id):
    teacher = Teacher.objects.get(id=id)

    form = TeacherForm()
    form.initial = {
        "name" : teacher.name,
        "dni" : teacher.dni
    }

    return render(request, "teachers/update_teacher.html", {
        "form" : form,
        "teacher_id" : teacher.id
    })

def update_teacher(request, id):
    teacher = Teacher.objects.get(id=id)
    if request.method == "POST":
        form = TeacherForm(request.POST)
        teacher.name = request.POST['name']
        teacher.dni = request.POST['dni']
        teacher.save()
        
        return render(request, "teachers/update_teacher.html", {
            "msg" : "Updated successfully",
            "success"  : True,
            "form" : TeacherForm(request.POST),
            "teacher_id" : teacher.id
        })        

    else:
        return render(request, "teachers/update_teacher.html", {
            "msg" : "An error ocurred during the process",
            "success" : False,
            "form" : UserForm(request.POST),
            "teacher_id" : teacher.id
        })
        

def delete_teacher(request, id):
    teacher = Teacher.objects.get(id=id).delete()
    return HttpResponseRedirect(reverse('list-all-teachers'))

def update_teacher_state(request, id):
    teacher = Teacher.objects.get(id=id)
    teacher.is_active = False if teacher.is_active else True
    teacher.save()
    return HttpResponseRedirect(reverse('list-all-teachers')) 

def list_all_teachers(request):
    teachers = Teacher.objects.all()
    return render(request, "teachers/all_teachers.html", {
        "teachers" : teachers
    })

def get_teacher_count():
    return Teacher.objects.all().count()