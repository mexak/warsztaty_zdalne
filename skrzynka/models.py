from django.db import models

# Create your models here.


class Person(models.Model):
	name = models.CharField(max_length=64)
	surname = models.CharField(max_length=128)
	description = models.TextField()

class Address(models.Model):
	city = models.CharField(max_length=64)
	street = models.CharField(max_length=64)
	apt = models.SmallIntegerField()
	person = models.ForeignKey(Person)

class Phone(models.Model):
	phone_number = models.SmallIntegerField()
	phone_type = models.CharField(max_length=64)
	person = models.ForeignKey(Person)

class Email(models.Model):
	email = models.CharField(max_length=64)
	email_type = models.CharField(max_length=64)
	person = models.ForeignKey(Person)

class Groups(models.Model):
	person = models.ManyToManyField(Person)



