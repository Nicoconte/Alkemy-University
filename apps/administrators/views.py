from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Administrator

from apps.common.forms import UserForm
from apps.common.utils import validate_url

from apps.public import urls

from apps.teachers.views import get_teacher_count
from apps.subjects.views import get_subjects_count
from apps.students.views import get_student_count

# Create your views here.
def administrator_login(request):
    if request.method == "POST":
        form = UserForm(request.POST)

        if form.is_valid():
            name = request.POST['name']
            password = request.POST['password']
            
            user = authenticate(request, username=name, password=password)

            if user:        

                admin = None
                
                try: 
                    admin = Administrator.objects.get(user=user)
                except Administrator.DoesNotExist:
                    return render(request, "administrators/admin_login.html", {
                        "form" : form,
                        "msg" : "The account introduced is not an administrator account"
                    })

                login(request, user)

                request.session['current_user'] = {
                    "token" : str(admin.token),
                    "role" : admin.role
                }

                return HttpResponseRedirect(reverse('administrator-dashboard'))
            
            else:
                return render(request, "administrators/admin_login.html", {
                    "msg" : "Invalid credentials",
                    "form" : form
                })

        else:
            return render(request, "administrators/admin_login.html", {
                "msg" : "Invalid data",
                "form" : form
            })
    else:
        return render(request, "administrators/admin_login.html", {
            "form" : UserForm()
        })

def administrator_logout(request):
    if 'current_user' in request.session:
        del request.session['current_user']
    
    logout(request)

    return HttpResponseRedirect(reverse('login'))

def dashboard(request):

    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))

    if 'current_user' in request.session:
        if request.session['current_user']['role'] == "student":
            return HttpResponseRedirect(reverse('student-dashboard'))

    return render(request, "administrators/admin_dashboard.html", {
        "token" : request.session['current_user']['token'],
        "teacher_count" : get_teacher_count(),
        "subject_count" : get_subjects_count(),
        "student_count" : get_student_count()    
    })
 