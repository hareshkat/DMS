from django.urls import path
from django.conf.urls import url
from employee import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/', views.login_view, name="account_login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('employees', views.employees, name='employees'),
    url(r'employees_list', views.employees_list, name='employees_list'),
    path('departments', views.departments, name = 'departments'),
    url(r'departments_list', views.departments_list, name='departments_list'),
    path('departments/<str:dept_id>/employees', views.department_employees, name='dept_emps'),
]
