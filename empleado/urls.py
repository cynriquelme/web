from django.contrib import admin
from django.urls import path, re_path, include
from applications.home.views import Home

urlpatterns = [
    path('admin/', admin.site.urls),
    #Incluimos las urls de la app departamento
    re_path('', include('applications.departamento.urls')),
    re_path('', include('applications.persona.urls')),
    path('', Home.as_view(), name="home"),
]
