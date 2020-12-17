from django.urls import path, include

from . import views

urlpatterns = [
    path("new/", views.teacher_form, name="new-teacher"),
    path("new/create/", views.create_teacher, name="create-new-teacher"),
    path("delete/<int:id>/", views.delete_teacher, name="delete-teacher"),
    path("update-state/<int:id>/", views.update_teacher_state, name='update-teacher-state'),
    path('<int:id>/', views.teacher_form_update, name='get-teacher-data'),
    path('change/<int:id>/', views.update_teacher, name='update-teacher'),
    path("all/", views.list_all_teachers, name="list-all-teachers")
]
