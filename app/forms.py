from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    #required_css_class = 'form-control'

    class Meta:
        model = Contact
        fields = ('name', 'email', 'company', 'phone', 'message',)
