from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import  Submit

class ContactForm(forms.Form):
	full_name = forms.CharField(required=False)
	email = forms.EmailField()
	message = forms.CharField()

	helper = FormHelper()
	helper.form_method = 'POST'
	helper.add_input(Submit('submit','submit',css_class='btn-primary'))