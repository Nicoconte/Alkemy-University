from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from apps.common.forms import UserForm
from apps.common.utils import *

# Create your views here.
def home(request):
    return render(request, "public/home.html")

def login(request):
    if 'current_user' in request.session:
        if request.session['current_user']['role'] == "student":
            return HttpResponseRedirect(reverse('student-dashboard'))
        else:
            return HttpResponseRedirect(reverse('administrator-dashboard'))

    return render(request, "public/login.html") 

def login_form_student(request):
    if 'current_user' in request.session:
        if request.session['current_user']['role'] == "student":
            return HttpResponseRedirect(reverse('student-dashboard'))
        else:
            return HttpResponseRedirect(reverse('administrator-dashboard'))

    return render(request, "students/student_login.html", {
        "form" : UserForm()   
    })

def login_form_admin(request):
    if 'current_user' in request.session:
        if request.session['current_user']['role'] == "student":
            return HttpResponseRedirect(reverse('student-dashboard'))
        else:
            return HttpResponseRedirect(reverse('administrator-dashboard'))

    return render(request, "administrators/admin_login.html", {
        "form" : UserForm()
    })