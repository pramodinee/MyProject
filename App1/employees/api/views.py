from employees.models import Employee
from employees.api.serializer import EmployeeSerializers

from rest_framework import viewsets

class EmployeeModalViewsets(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers