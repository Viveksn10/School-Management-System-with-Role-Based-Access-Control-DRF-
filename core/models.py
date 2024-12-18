
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'School Admin'),
        ('office_staff', 'Office Staff'),
        ('librarian', 'Librarian')
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return self.username

class Student(models.Model):
    full_name = models.CharField(max_length=100)
    class_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    roll_number = models.CharField(max_length=10)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.full_name} ({self.roll_number})"

class LibraryHistory(models.Model):
    STATUS_CHOICES = (
        ('borrowed', 'Borrowed'),
        ('returned', 'Returned'),
        ('overdue', 'Overdue')
    )
    
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='library_records')
    book_name = models.CharField(max_length=200)
    borrow_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='borrowed')
    
    def __str__(self):
        return f"{self.student} - {self.book_name}"

class FeesHistory(models.Model):
    FEE_TYPES = (
        ('tuition', 'Tuition'),
        ('library', 'Library Fee'),
        ('exam', 'Exam Fee'),
        ('other', 'Other')
    )
    
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='fees_records')
    fee_type = models.CharField(max_length=20, choices=FEE_TYPES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()
    remarks = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.student} - {self.fee_type} Fee"