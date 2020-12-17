from django.urls import path, include

from . import views

from apps.students import views as student_view

urlpatterns = [
    path("auth/", views.administrator_login, name="administrator-auth"),
    path('administrator/logout', views.administrator_logout, name="administrator-logout"),
    path("dashboard/", views.dashboard, name="administrator-dashboard"),
    path("dashboard/", include("apps.teachers.urls")),
    path('dashboard/subject/', include('apps.subjects.urls')),

    #TODO: Incluir las urls de la aplicacion estudiante excluyendo la autenticacion y el acceso al dashboard
    path("dashboard/student/all/", student_view.list_all_students, name="list-all-students"),
    path("dashboard/student/new/", student_view.student_form, name="new-student"),
    path("dashboard/student/new/create/", student_view.create_student, name="create-student"),
    path("dashboard/student/delete/<int:id>/", student_view.delete_student, name="delete-student"),
    path("dashboard/student/<int:id>", student_view.student_form_update, name="update-student"),
    path("dashboard/student/update/<int:id>", student_view.update_student, name="update-current-student")
]
