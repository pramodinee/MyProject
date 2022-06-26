from django.urls import path
from employees import views


urlpatterns = [

    path('',views.EmployeeListView.as_view() ,name='employee'),
    path('create', views.EmployeeCreateView.as_view(), name='employeeCreate'),
    path('<int:pk>/detail',views.EmployeeDetailView.as_view(),name='employeeDetail'),
    path('<int:pk>/update',views.EmployeeUpdateView.as_view(),name='employeeUpdate'),
    path('<int:pk>/delete',views.EmployeeDeleteView.as_view(),name='employeeDelete'),

]