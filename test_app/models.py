from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=20)
    department = models.CharField(max_length=20)
    semester = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=11)

    # using this string method it will show the returned object which i returned rather than showing only object of that table.
    def __str__(self):
        return self.name + " /" + self.department


class Course(models.Model):
    st = models.ForeignKey(Student, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=20)
    credit = models.IntegerField()

    def __str__(self):
        return self.course_name