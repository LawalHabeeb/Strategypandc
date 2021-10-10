
from django import forms

class ContactForm(forms.Form):
    full_name = forms.CharField(max_length=75, widget=forms.TextInput(attrs={"class": "form-control form-cont", "placeholder": "Full name", "required": "true"}))
    email_address = forms.EmailField(max_length=90, widget=forms.EmailInput(attrs={"class": "form-control form-cont", "placeholder": "Email address", "required": "true"}))
    company_name = forms.CharField(max_length=90, widget=forms.TextInput(attrs={"class": "form-control form-cont", "placeholder": "Company name", "required": "false"}))
    message = forms.CharField(widget=forms.Textarea(attrs={"class": "form-cont", "placeholder": "Type your message here", "required": "true"}))
