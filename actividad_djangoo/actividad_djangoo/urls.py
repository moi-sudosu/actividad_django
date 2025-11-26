from django.contrib import admin
from django.urls import path
from web import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pruebas/', views.vista_pruebas),
    path('template/', views.vista_template),
]