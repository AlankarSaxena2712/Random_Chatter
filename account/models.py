from django.db import models
# Create your models here.

GENDER_CHOICES = (
	('1', 'Male'),
	('2', 'Female'),
	('3', 'Transgender'),
	('4', 'Not specify')
)

class User(models.Model):
	user_name = models.CharField(max_length=50)
	password = models.CharField(max_length=32)
	gender = models.CharField(choices=GENDER_CHOICES, max_length=1)
	def __str__(self):
		return self.user_name

