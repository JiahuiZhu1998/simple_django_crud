from django.contrib import admin

# Register your models here.
from django.contrib import admin
from app1.models import Student, Teacher, Class

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ['student_Name', 'student_Class']
admin.site.register(Student,StudentAdmin)

class TeacherAdmin(admin.ModelAdmin):
    list_display = ['teacher_Name', 'get_teacher_class']
admin.site.register(Teacher,TeacherAdmin)

class ClassAdmin(admin.ModelAdmin):
    list_display = ['class_Name']
admin.site.register(Class,ClassAdmin)

