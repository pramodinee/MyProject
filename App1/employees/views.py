from django.shortcuts import render
from employees.forms import EmployeeForms
from employees.models import Employee
from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView

class EmployeeListView(ListView):
    model = Employee
    #template_name = 'employee/employee_list.html'
    #content = employee_list

class EmployeeDetailView(DetailView):
    model = Employee
    # template_name = 'employee/employee_detail.html'
    # content = employee | object

class EmployeeCreateView(CreateView):
    model = Employee
    fields = '__all__'
    # template_name = 'employee/employee_form.html'
    # content = form

class EmployeeUpdateView(UpdateView):
    model = Employee
    fields = '__all__'
    # template_name = 'employee/employee_form.html'
    # content = form

class EmployeeDeleteView(DeleteView):
    model = Employee
    success_url = '/employee/'
    # template_name = 'employee/employee_confirm_delete.html'
    # content = employee | object