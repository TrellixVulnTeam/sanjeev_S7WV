from __future__ import unicode_literals

from django.db import models

# Create your models here.
class InvoicePdf(models.Model):
	invoice_id = models.AutoField(primary_key=True)
	customer_name = models.CharField(max_length=20)
	amount = models.IntegerField()
	Date = models.DateField(auto_now_add=True)