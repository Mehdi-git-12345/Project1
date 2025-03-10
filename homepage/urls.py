from django.urls import path
from .views import hello, insertEmployee, getEmployee, addEmployee
urlpatterns = [
    path("hello2/",hello),
    path('insert/', insertEmployee, name='insertEmployee'),
    path('api/employees',getEmployee, name='getEmployee'),
    path('api/employees/add',addEmployee, name='addEmployee'),


]