from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Entry(models.Model):
	email = models.EmailField()
	problem = models.TextField(max_length=1000)
		
	class Admin: 
		pass
	
	def __str__(self):
		return self.email
		
