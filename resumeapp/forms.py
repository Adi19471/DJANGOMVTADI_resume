from django import forms
from django.db import models
from django.forms import fields, widgets

from .models import Resume

GENDER_CHOICES = [
    ('Mail','Male'),
    ('Female','Female')
]

JOB_CITY_CHOICE = [
    ('Andra Pradesh','Amaravathi'),
    ('Hyderbad','Hyderabad'),
    ('NewDelhi','Delhi'),
    ('Banglore','Banglore'),

]
class ResumeForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=GENDER_CHOICES,widget=forms.RadioSelect)
    city = forms.MultipleChoiceField(label='Prefered Job Locatin',choices=JOB_CITY_CHOICE,widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Resume
        fields = '__all__'

        labels = {'name':'Full Name','dob':'Date of Borth',
        'email':'Emial ID',
        'gender':'Gender','Locality':'Your Location','city':'Your City',
        'state':'Select Your States','Job location':'Job Location',
        'profile_image':'Your Image',
        'my_file':'Your Resume'  
        }


        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'dob':forms.DateInput(attrs={'class':'form-control','id':'datepicker'}),
            
            'locality':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'pincode':forms.NumberInput(attrs={'class':'form-control'}),
            'state':forms.Select(attrs={'class':'form-select'}),
            'mobile':forms.NumberInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'job_location':forms.TextInput(attrs={'class':'form-control'}),
            # 'profile_image':forms.TextInput(attrs={'class':'form-control'}),
            'job_state':forms.TextInput(attrs={'class':'form-control'}),
            # 'my_file':forms.(attrs={'class':'form-control'}),
        }
