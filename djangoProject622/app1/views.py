from django.shortcuts import render,redirect,reverse
from .models import Student,Teacher,Class
from .forms import StudentForm,TeacherForm, ClassForm
# Create your views here.


## home page
def home_page_student(request):
	students = Student.objects.all()  # retrive operation
	teachers = Teacher.objects.all()
	classes = Class.objects.all()
	return render(request, 'student.html', {'students': students, 'teachers': teachers, 'classes': classes})

###
### class
###
def add_view_cls(request):
	if request.method == 'POST':
		form = ClassForm(request.POST)
		if form.is_valid():
			#new_class_No = form.cleaned_data['class_No']
			new_class_Name = form.cleaned_data['class_Name']
			new_class = Class(class_Name=new_class_Name)
			new_class.save()
			return render(request, 'add_class.html', {'form':ClassForm, 'success':True})
	else:
		form = ClassForm()
	return render(request, 'add_class.html', {'form':ClassForm()})
def delete_view_cls(request, id):
	class1 = Class.objects.get(id=id)
	class1.delete()
	return redirect('/')
def update_view_cls(request, id):
	if request.method == 'POST':
		class1 = Class.objects.get(pk=id)
		form = ClassForm(request.POST, instance=class1)
		if form.is_valid():
			form.save()
			return render(request, 'update_class.html', {'form': form,'success': True})
	else:
		class1 = Class.objects.get(pk=id)
		form = ClassForm(instance=class1)
	return render(request, 'update_class.html', {'form': form})


###
###  teacher
###
def add_view_tea(request):
	if request.method == 'POST':
		form = TeacherForm(request.POST)
		if form.is_valid():
			new_teacher = Teacher()
			new_teacher_Name = form.cleaned_data['teacher_Name']
			new_teacher_Classes = form.cleaned_data['teacher_Class']
			new_teacher = Teacher(teacher_Name=new_teacher_Name)
			new_teacher.save()
			for class1 in new_teacher_Classes:
				new_teacher.teacher_Class.add(class1)
			#new_teacher.teacher_Class.set(new_teacher_Classes)
			new_teacher.save()
			return render(request, 'add_teacher.html', {'form':TeacherForm, 'success':True})
	else:
		form = TeacherForm()
	return render(request, 'add_teacher.html', {'form':TeacherForm()})
def delete_view_tea(request,id):
	teacher1 = Teacher.objects.get(id=id)
	teacher1.delete()
	return redirect('/')
def update_view_tea(request,id):
	if request.method == 'POST':
		teacher1 = Teacher.objects.get(pk=id)
		form = TeacherForm(request.POST, instance=teacher1)
		if form.is_valid():
			form.save()
			return render(request, 'update_teacher.html', {'form': form,'success': True})
	else:
		teacher1 = Teacher.objects.get(pk=id)
		form = TeacherForm(instance=teacher1)
	return render(request, 'update_teacher.html', {'form': form})

###
###  student
###
def add_view_stu(request):
	if request.method == 'POST':
		form = StudentForm(request.POST)
		if form.is_valid():
			new_student_name = form.cleaned_data['student_Name']
			#new_student = Student(student_Name=new_student_name)
			#new_student.save()
			new_student = Student(student_Name=new_student_name,student_Class=form.cleaned_data['student_Class'])
			new_student.save()
			return render(request, 'add_student.html', {'form': StudentForm, 'success': True})
	else:
		form = StudentForm()
	return render(request, 'add_student.html', {'form': StudentForm()})
def delete_view_stu(request,id):
	student1 = Student.objects.get(id=id)
	student1.delete()
	return redirect('/')
def update_view_stu(request,id):
	if request.method == 'POST':
		student1 = Student.objects.get(pk=id)
		form = StudentForm(request.POST, instance=student1)
		if form.is_valid():
			form.save()
			return render(request, 'update_student.html', {'form': form, 'success': True})
	else:
		student1 = Student.objects.get(pk=id)
		form = StudentForm(instance=student1)
	return render(request, 'update_student.html', {'form': form})