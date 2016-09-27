from django.db import models

# Create your models here.
class User(models.Model):
	name = models.CharField(max_length=20)
	password = models.CharField(max_length=20)
	email = models.CharField(max_length=30)
	cellphone = models.CharField(max_length=15)

	def __str__(self):
		return self.name

	class Meta:
		db_table = 'User'