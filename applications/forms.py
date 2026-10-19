from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Application, Company
class RegisterForm(UserCreationForm):
 email=forms.EmailField(required=False)
 class Meta:
  model=User
  fields=("username","email","password1","password2")
class CompanyForm(forms.ModelForm):
 class Meta:
  model=Company
  fields=("name","website","location")
  widgets={"name":forms.TextInput(attrs={"placeholder":"e.g. Zoho"}),"website":forms.URLInput(attrs={"placeholder":"https://company.com"}),"location":forms.TextInput(attrs={"placeholder":"Chennai, India"})}
class ApplicationForm(forms.ModelForm):
 class Meta:
  model=Application
  fields=("company","role","applied_on","status","job_url","notes")
  widgets={"applied_on":forms.DateInput(attrs={"type":"date"}),"role":forms.TextInput(attrs={"placeholder":"e.g. Python Developer"}),"job_url":forms.URLInput(attrs={"placeholder":"https://..."}),"notes":forms.Textarea(attrs={"rows":3,"placeholder":"Interview notes, follow-up dates..."})}
