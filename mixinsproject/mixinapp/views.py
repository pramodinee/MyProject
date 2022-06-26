from django.shortcuts import render
from .models import Employee
from .serializer import EmployeeSerializer
from rest_framework import mixins,generics

class EmployeeListView(mixins.ListModelMixin,
                       mixins.CreateModelMixin,
                       generics.GenericAPIView
                       ):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)

class EmployeeDatilsView(mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.DestroyModelMixin,
                         generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get(self,request,pk):
        return self.retrieve(request)
    def put(self,request,pk):
        return self.update(request)
    def delete(self,request,pk):
        return self.delete(request)
