from .models import Student, Teacher, Class
from django import forms


class StudentForm(forms.ModelForm):
	class Meta:
		model = Student
		#exclude = ('student_Class',)
		fields = '__all__'

class TeacherForm(forms.ModelForm):
	class Meta:
		model = Teacher
		fields = '__all__'

class ClassForm(forms.ModelForm):
	class Meta:
		model = Class
		fields = '__all__'
