from django.db import models

# Create your models here.

class Book(models.Model):
	bname=models.CharField(max_length=100)
	author=models.CharField(max_length=100)
	price=models.IntegerField()
	category=models.CharField(max_length=100)
	def __str__(self):
		return self.bname