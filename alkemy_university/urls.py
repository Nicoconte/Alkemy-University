from django.contrib import admin
from django.urls import path, include

from apps.public import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("apps.public.urls")),
    path('student/', include('apps.students.urls')),
    path('administrator/', include('apps.administrators.urls'))
]
