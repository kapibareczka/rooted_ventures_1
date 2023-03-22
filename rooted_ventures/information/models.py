from django.db import models

# Create your models here.


class ContactForm(models.Model):
	first_name = models.CharField(max_length = 50)
	last_name = models.CharField(max_length = 50)
	email_address = models.EmailField(max_length = 150)
	message = models.CharField(max_length=10000)