# forms.py
from django import forms
from .models import *

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'skills', 'contact_details']

class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ['projects', 'work_experience', 'education', 'certifications']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'image', 'link']
