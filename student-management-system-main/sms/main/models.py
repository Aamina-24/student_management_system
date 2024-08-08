from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class AboutPage(models.Model):
    about = models.TextField()

    def __str__(self):
        return self.about

class ContactPage(models.Model):
    address = models.TextField()
    contact_num = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.address


class Student(models.Model):
    full_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=50, default="Male")
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    email = models.EmailField()
    contact_num = models.CharField(max_length=10)
    date_of_birth = models.DateField()
    course = models.CharField(max_length=50)
    stu_id = models.CharField(max_length=50)
    
    user_name = models.CharField(max_length=50)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name


class Notice(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    isPublic = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Teacher(models.Model):
    full_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=50)
    email = models.EmailField()
    contact_num = models.CharField(max_length=20)
    qualification = models.TextField()

    def __str__(self):
        return self.full_name
    


class Feedback(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    


class LeaveRequest(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]
    
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    reason = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.student.username} - {self.status}'
  