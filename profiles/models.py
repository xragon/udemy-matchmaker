from django.db import models
from django.contrib.auth.models import User

class Address(models.Model):
	user = models.ForeignKey(User)
	street_address = models.CharField(max_length=200)
	city = models.CharField(max_length=200)
	state = models.CharField(max_length=200)
	zipcode = models.CharField(max_length=5)
	active = models.BooleanField(default=True)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

	def __unicode__(self):
		return self.city

class Job(models.Model):
	user = models.ForeignKey(User)
	postion = models.CharField(max_length=100)
	employer = models.CharField(max_length=200)
	street_address = models.CharField(max_length=200)
	city = models.CharField(max_length=200)
	state = models.CharField(max_length=200)
	zipcode = models.CharField(max_length=5)
	phone = models.CharField(null=True, blank=True, max_length=20)

	start_date = models.DateTimeField(auto_now=False, auto_now_add=False)
	end_date = models.DateTimeField(auto_now=False, auto_now_add=False)

	active = models.BooleanField(default=True)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

	def __unicode__(self):
		return self.postion
    
class UserPicture(models.Model):
	user = models.ForeignKey(User)
	image = models.ImageField(upload_to='profiles/')

	active = models.BooleanField(default=True)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

	def __unicode__(self):
		return str(self.image)