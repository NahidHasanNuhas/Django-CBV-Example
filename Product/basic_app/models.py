from django.db import models
from django.urls import reverse
# Create your models here.

class Product(models.Model):
	Name = models.CharField(max_length=256)
	Company = models.CharField(max_length=256)
	Published = models.DateField()
	Price = models.PositiveIntegerField()

	def __str__(self):
		return self.Name

	def get_absolute_url(self):
		return reverse('basic_app:product_detail', kwargs={'pk':self.pk})
