
from django.urls import path
from mixinapp import views


urlpatterns = [
    path('employee/',views.EmployeeListView.as_view()),
    path('employee/<int:pk>/',views.EmployeeDatilsView.as_view()),
]