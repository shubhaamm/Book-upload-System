from django.db import models

# Create your models here.

class Class_name(models.Model):
      first_name = models.CharField(max_length=20)  
      last_name  = models.CharField(max_length=30)  
      contact    = models.IntegerField()  
      email      = models.EmailField(max_length=50)  
      password   = models.IntegerField()

class Book(models.Model):
      title = models.CharField(max_length=100)  
      author  = models.CharField(max_length=100) 
      pdf =models.FileField(upload_to='books/pdfs/') 


      def __str__(self):
          return self.title

      
