from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from home.models import Contact


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)


#class ContactForm(forms.ModelForm):
#    
#    class Meta:
#        model = Contact
#        fields = ['first_name', 'last_name', 'email', 'message']
#        
#        def __init__(self, *args, **kwargs):
#            super().__init__(*args, **kwargs)
#            self.helper = FormHelper()
#            self.helper.form_method = 'post'
#            self.helper.add_input(Submit('submit', 'SEND'))
#
#        def __str__(self):
#            return self.email