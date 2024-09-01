from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.signup),
    path('login/', views.user_logn),
    path('todo/', views.todo),
    path('edit_todo/<int:srno>', views.edit_todo, name='edit_todo'),
    path('delete_todo/<int:srno>', views.delete_todo)
]
