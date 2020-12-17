from django.urls import path, include

from . import views

urlpatterns = [
    path("auth/", views.student_login, name="student-auth"),
    path('logout', views.student_logout, name='student-logout'),
    path("dashboard/", views.dashboard, name="student-dashboard"),
    path("dashboard/my-subjects/", views.my_subjects, name="my-subjects"),
    path("dashboard/inscriptions", views.inscriptions, name="inscriptions"),
    path("dashboard/inscriptions/subscrite-to/<int:id>", views.subscribe_to, name="subscribe-to")
]
