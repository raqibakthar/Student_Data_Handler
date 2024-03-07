from django.contrib import admin
from .models import Student
# Register your models here.

class MemberView(admin.ModelAdmin):
    list_display=('id','first_name','last_name')

admin.site.register(Student,MemberView)
