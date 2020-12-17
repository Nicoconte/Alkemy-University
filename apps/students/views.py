from apps.subjects.models import Subject
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse


from .models import Student, StudentSubject
from .forms import StudentForm

from apps.common.forms import UserForm
from apps.common.utils import get_random_email, get_random_number

from apps.public import urls

from apps.subjects.models import Subject
from apps.subjects.views import update_subject_capacity

from faker import Faker
import random as r

# Create your views here.

def student_login(request):
    if request.method == "POST":
        form = UserForm(request.POST)

        if form.is_valid():
            name = request.POST['name']
            password = request.POST['password']
            
            user = authenticate(request, username=name, password=password)

            if user:
                
                student = None

                #TODO: Refactor this or get in into a function. Verify if the student exist in the table "Student" 
                try:
                    student = Student.objects.get(student_account=user)

                except Student.DoesNotExist:
                    return render(request, "students/student_login.html", {
                        "form" : form,
                        "msg" : "The account introduced does not exist as student account"
                    })
                
                login(request, user)

                request.session['current_user'] = {
                    "token" : str(student.token),
                    "role" : student.role
                }

                return HttpResponseRedirect(reverse('student-dashboard'))
            else:
                return render(request, "students/student_login.html", {
                    "msg" : "Invalid credentials",
                    "form" : form
                })

        else:
            return render(request, "students/student_login.html", {
                "msg" : "Invalid data",
                "form" : form
            })
    else:
        return render(request, "students/student_login.html", {
            "form" : UserForm()
        })


def student_logout(request):
    if request.session['current_user'] != None:
        del request.session['current_user']
        
    logout(request)
    return HttpResponseRedirect(reverse('login'))

def dashboard(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    
    if 'current_user' in request.session:
        if request.session['current_user']['role'] == "administrator":
            return HttpResponseRedirect(reverse('administrator-dashboard'))

    return render(request, "students/student_dashboard.html", {
        "msg" : "Hola, soy un estudiante", 
        "token" : request.session['current_user']['token']
    })


def student_form(request):
    return render(request, "students/create_student.html", {
        "form" : StudentForm
    })


def create_student(request):
    fake = Faker()

    if request.method == "POST":
        form = StudentForm(request.POST)

        user = User.objects.create_user(str(r.randint(1000000, 3000000)), fake.email(), request.POST['dni'])
        student = Student(name=request.POST['name'], dni=request.POST['dni'], student_account=user)

        print(f"Nombre => {student.name} Token? => {str(student.token)}")

        student.save()

        return render(request, "students/create_student.html", {
            "form" : StudentForm(),
            "success" : True,
            "msg" : "Created successfully", 
        })
    
    else:
        return render(request, "students/create_student.html", {
            "form" : StudentForm(request.POST),
            "success" : False,
            "msg" : "An error ocurred during process", 
        })


#*This functions will be execute by administrator in his dashboard
def list_all_students(request):
    students = Student.objects.all()
    return render(request, "students/all_students.html", {
        "students" : students
    })


def delete_student(request, id):
    User.objects.get(id=id).delete()
    return HttpResponseRedirect(reverse('list-all-students'))

def student_form_update(request, id):
    student = Student.objects.get(id=id)

    form = StudentForm()

    form.initial = {
        "name" : student.name,
        "dni" : student.dni
    }

    return render(request, "students/update_student.html", {
        "form" : form,
        "student_id" : student.id
    })

def update_student(request, id):
    
    student = Student.objects.get(id=id)
    form = StudentForm(request.POST)

    if request.method == "POST":
        student.name = request.POST['name']
        student.dni = request.POST['dni']

        student.save()

        return render(request, "students/update_student.html", {
            "form" : form,
            "msg" : "Updated successfully",
            "success" : True,
            "student_id" : student.id
        })
    else:
        return render(request, "students/update_student.html", {
            "form" : form,
            "msg" : "An error ocurred during the process",
            "success" : False,
            "student_id" : student.id
        })        

def get_student_count():
    return Student.objects.all().count()


def my_subjects(request):
    student = Student.objects.get(token=request.session['current_user']['token'])
    student_subjects = StudentSubject.objects.filter(student=student).order_by("subject")

    return render(request, "subjects/my_subjects.html", {
        "my_subjects" : student_subjects
    })


def inscriptions(request):
    return render(request, "subjects/list_subjects.html", {
        "subjects" : Subject.objects.all().order_by('name')
    })


def schedule_match_with(subject, student):
    schedules = [subject.subject.schedule for subject in StudentSubject.objects.filter(student=student)]

    if subject.schedule in schedules:
        return True
    
    return False

def already_subscribe_to(subject, student):
    inscriptions = [subject.subject.name for subject in StudentSubject.objects.filter(student=student)]

    if subject.name in inscriptions:
        return True
    
    return False

def there_is_space(subject):
    if subject.capacity <= 0:
        return False
    return True

def subscribe_to(request, id):
    subject = Subject.objects.get(id=id)
    student = Student.objects.get(token=request.session['current_user']['token'])

    if schedule_match_with(subject, student):
        return render(request, "subjects/list_subjects.html", {
            "success" : False,
            "msg" : "El horario coincide con otra",
            "subjects" : Subject.objects.all().order_by("name")
        })

    if already_subscribe_to(subject, student):
        return render(request, "subjects/list_subjects.html", {
            "success" : False,
            "msg" : f"Ya estas inscripto a la materia {subject.name}",
            "subjects" : Subject.objects.all().order_by("name")
        })

    if not there_is_space(subject):
        render(request, "subjects/list_subjects.html", {
            "success" : False,
            "msg" : "No hay cupos disponibles",
            "subjects" : Subject.objects.all().order_by("name")
        })

    student_subject = StudentSubject(student=student, subject=subject)
    student_subject.save()

    update_subject_capacity(subject.id)

    return HttpResponseRedirect(reverse("my-subjects"))


    