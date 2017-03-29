from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ['name', 'email', 'company', 'phone', 'message']
        widgets = {
            'name': forms.TextInput(
                attrs={'id': 'id_name', 'required': True,
                       'placeholder': 'Full Name',
                       'class' : 'form-control', 'type' : 'text'}
            ),
            'email': forms.TextInput(
                attrs={'id': 'id_email', 'required': True,
                       'placeholder': 'E-Mail Address',
                       'class': 'form-control', 'type': 'text'}
            ),
            'company': forms.TextInput(
                attrs={'id': 'id_company', 'required': True,
                       'placeholder': 'Your company',
                       'class': 'form-control', 'type': 'text'}
            ),
            'phone': forms.TextInput(
                attrs={'id': 'id_phone', 'required': True,
                       'placeholder': '(845)555-1212',
                       'class': 'form-control', 'type': 'text'}
            ),
            'message': forms.TextInput(
                attrs={'id': 'id_message', 'required': True,
                       'placeholder': 'Your message',
                       'class': 'form-control', 'type': 'text'}
            ),
        }