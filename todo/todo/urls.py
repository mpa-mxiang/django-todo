from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.signup),
    path('login/', views.user_logn),
    path('todo/', views.todo)
]
