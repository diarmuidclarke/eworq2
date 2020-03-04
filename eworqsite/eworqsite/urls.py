from django.contrib import admin
from django.urls import include,path

urlpatterns = [
    path('eworqapp/', include('eworqapp.urls')),
    path('admin/', admin.site.urls),
]
