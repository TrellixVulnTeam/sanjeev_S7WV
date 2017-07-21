from django.contrib import admin

# Register your models here.

from .models import *
admin.site.site_header = "My administration"

class Invoicemodeladmin(admin.ModelAdmin):
	list_display = ["customer_name","Date"]
	class Meta:
		model=InvoicePdf
admin.site.register(InvoicePdf,Invoicemodeladmin)