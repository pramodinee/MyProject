from django.contrib import admin

from .models import Student,StudentProxy


class StudentAdmin (admin.ModelAdmin):
    list_display =['name','mark','location']

class StudentProxyAdmin (admin.ModelAdmin):
    list_display =['name','mark','location']

admin.site.register(Student,StudentAdmin )
admin.site.register(StudentProxy,StudentProxyAdmin)


