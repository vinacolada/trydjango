from django.db import models

# Create your models here.
class Product(models.Model):
	#refer to documentation for model fields
	title = models.CharField(max_length=120)
	description = models.TextField(blank=True, null=True)
	price = models.DecimalField(decimal_places=2, max_digits=1000)
	# blank=False means required, null=False means cannot be empty in database
	summary = models.TextField(blank=False, null=False)
	# when adding a new field, use null=True to leave the new field empty for the older data
	# or set default for all the previous data; you can use the command line to apply these
	featured = models.BooleanField()