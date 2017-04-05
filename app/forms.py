from django import forms
from django.forms import inlineformset_factory
from .models import Contact, ContactPhone
import re

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ['name', 'email', 'company', 'message']
        widgets = {
            'name': forms.TextInput(
                attrs={'id': 'id_name', 'required': True,
                       'placeholder': 'Full Name',
                       'class': 'form-control', 'type': 'text'}
            ),
            'email': forms.TextInput(
                attrs={'id': 'id_email',
                       'placeholder': 'E-Mail Address',
                       'class': 'form-control', 'type': 'text'}
            ),
            'company': forms.TextInput(
                attrs={'id': 'id_company', 'required': True,
                       'placeholder': 'Your company',
                       'class': 'form-control', 'type': 'text'}
            ),
            'message': forms.TextInput(
                attrs={'id': 'id_message', 'required': True,
                       'placeholder': 'Your message',
                       'class': 'form-control', 'type': 'text'}
            ),
        }

    # def clean(self):
    #     cleaned_data = super(ContactForm, self).clean()
    #     phone = cleaned_data.get("phone")
    #     email = cleaned_data.get("email")
    #
    #     if not phone and not email:
    #         raise forms.ValidationError("Enter phone or email")
    #
    #     return cleaned_data



class PhoneForm(forms.ModelForm):

    class Meta:
        model = ContactPhone
        fields = ['phone']
        widgets = {
            'phone': forms.TextInput(
                attrs={'id': 'id_phone',
                       'placeholder': '(845)555-1212',
                       'class': 'form-control', 'type': 'text'}
            )
        }

    def clean_phone(self):
        data = self.cleaned_data['phone']
        rule = re.compile(r'^(?:\+?44)?[07]\d{9,13}$')
        if data:
            if not rule.search(data):
                raise forms.ValidationError("Invalid phone number")
        return data

ContactPhoneFormSet = inlineformset_factory(Contact,
    ContactPhone, form=PhoneForm, extra=2, can_delete= True)
