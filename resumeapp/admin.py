from django.contrib import admin

# Register your models here.

from .models import Resume


@admin.register(Resume)
class ResumeModel(admin.ModelAdmin):
    list_display = ['id','name','dob','gender','city','pincode','state','mobile','email','job_location','profile_image','job_state','my_file']
