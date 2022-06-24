from django.db import models

# Create your models here.
class Class(models.Model):
	#class_No = models.PositiveIntegerField()
	class_Name = models.CharField(max_length=64)
	# class_stu_No = models.ForeignKey(Student, on_delete=models.CASCADE, default=1)
	# class_tea_No = models.ManyToManyField(Teacher)

	def __str__(self):
		return self.class_Name

class Student(models.Model):
	#stu_No = models.PositiveIntegerField()
	student_Name = models.CharField(max_length=64)
	student_Class = models.ForeignKey(Class, on_delete=models.CASCADE, default=1)

class Teacher(models.Model):
	#teacher_No = models.PositiveIntegerField()
	teacher_Name = models.CharField(max_length=64)
	teacher_Class = models.ManyToManyField(Class)

	def get_teacher_class(self):
		return ",".join([str(p) for p in self.teacher_Class.all()])


