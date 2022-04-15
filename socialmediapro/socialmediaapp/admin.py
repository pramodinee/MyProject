from django.contrib import admin
from .models import post,Profile,Comment

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    list_display = ('title','slug','author')

class AdminProfile(admin.ModelAdmin):
    list_display = ['user','dob','photo']

class AdminComments(admin.ModelAdmin):
    list_display = ['content']

admin.site.register(post,PostAdmin)
admin.site.register(Profile,AdminProfile)
admin.site.register(Comment,AdminComments)