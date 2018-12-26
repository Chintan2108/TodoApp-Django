from django.urls import path
from . import views 

urlpatterns = [
    path('home', views.home, name='home'),
    path('add', views.addTodo, name='add'),
    path('complete/<todo_id>', views.completeTodoToggle, name='completetoggle'),
    path('deletecomplete', views.deleteCompleted, name='deleteCompleted'),
    path('deleteall', views.deleteAll, name='deleteall'),
    path('mailall', views.mailAll, name='mailall'),
]