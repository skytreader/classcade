from django.db import models

class Classes(models.Model):
	class_code = models.CharField(max_length=10)
	section = models.CharField(max_length=5)

class Students(models.Model):
	class_code = models.ForeignKey(Classes)
	student_no = models.IntegerField()
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
