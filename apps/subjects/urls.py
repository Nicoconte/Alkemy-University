from django.urls import path, include

from . import views

urlpatterns = [
    path("all/", views.list_all_subjects, name='list-all-subjects'),
    path("new/", views.subject_form, name='new-subject'),
    path('new/create', views.create_subject, name='create-new-subject'),
    path('delete/<int:id>', views.delete_subject, name='delete-subject'),
    path('<int:id>', views.update_form, name="update-subject"),
    path('update/<int:id>', views.update_subject, name="update-current-subject")
]