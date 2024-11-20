from django.db import models

# Create your models here.

class Student(models.Model):
  studentid = models.AutoField(primary_key=True)
  student_name = models.CharField(max_length=30, null=True)
  course = models.CharField(max_length=30, null= True)
  section = models.IntegerField(null=True)
  image = models.FileField(upload_to='profile', null=True, blank=True)
  
  def __str__(self):
    return (self.student_name)
