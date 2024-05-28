from django import forms
#this allows us to create things like charfileds etc

from django.forms import ModelForm

from .models import Subscriber



#create a form that will allow a subscriber to subscribe
class RegisterSubscriberForm(forms.ModelForm):#making custom model form

    class Meta:
        model = Subscriber
        fields = ['first_name', 'last_name', 'email', 'phone', 'subscriber_residence']

        labels = {
            'first_name': '',
            'last_name': '',
            'email': '',
            'phone': '',
            'subscriber_residence': '',
        }

        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control col-lg-4','placeholder':'Enter first name' }),#this will allow bootstrap to tyle the form
           'last_name': forms.TextInput(attrs={'class':'form-control col-lg-4', 'placeholder':'Enter last name'}),
          'email': forms.TextInput(attrs={'class':'form-control col-lg-4', 'placeholder':'Enter email'}),
           'phone': forms.TextInput(attrs={'class':'form-control col-lg-4 ', 'placeholder':'Enter phone number'}),
           'city_of_residence': forms.Select(attrs={'class':'form-control col-lg-3'}),
        }