from django.shortcuts import render

from .forms import ContactForm

from django.http import HttpResponse
from django.views.generic import View
from .models import *
from .utils import render_to_pdf
from django.template.loader import get_template
# Create your views here.
def home(request):
	return render(request,'home.html',{})


def Contact(request):
	form = ContactForm(request.POST or None)
	if form.is_valid():
		for key,value in form.cleaned_data.iteritems():
			print key, value
		# email = form.cleaned_data.get("email")
		# message = form.cleaned_data.get("message")
		# full_name = form.cleaned_data.get("full_name")
		# print email,message,full_name
	context = {
	     "form": form,
	}




	return render(request,'forms.html',context)



def generate(request, *args, **kwargs):
	template = get_template('invoice.html')
	data = InvoicePdf.objects.all()
	context = {
	        "data": data,
	        	} 
	# html = template.render(context)
	pdf = render_to_pdf('invoice.html',context)
	        
	return HttpResponse(pdf,content_type='application/pdf')