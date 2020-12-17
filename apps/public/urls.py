from django.urls import path

from . import views

urlpatterns = [
    path('home', views.home, name="home"),
    path('login/', views.login, name="login"),
    path('login/student/', views.login_form_student, name="student-account-login"),
    path('login/administrator', views.login_form_admin, name="admin-account-login")
]