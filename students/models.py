from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.

class Student(models.Model):
    GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'), ('O', 'Other'))
    COURSE_CHOICES = (('IT', 'Information Technology'), ('CSE', 'Computer Science'), ('EEE', ''
                                                                                             'Electricals and Electronic Engineering'))
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    sex = models.CharField(max_length=1, choices=GENDER_CHOICES)
    email = models.EmailField(blank=False, unique=True)
    permanent_address = models.TextField(max_length=700)

    def __str__(self):
        return self.first_name

    # def was_a_9_pointer(self):
    #     if self.cgpa > 9.0:
    #         return True
    #     else:
    #         return False
