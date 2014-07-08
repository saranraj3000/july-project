from django.db import models
class Contact(models.Model):
	first_name=models.CharField(
		max_length=255,
		)
	last_name=models.CharField(
		max_length=255,
		)
	email1=models.CharField(
		max_length=255,
		)
	def __unicode__(self):
	  return ' '.join([
		self.first_name,
		self.last_name,
		self.email1,
		])
# Create your models here.
