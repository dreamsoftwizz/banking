from django import forms
from student.models import contact, registration, FAQs, courses, studymaterial,success,vacancy
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Create your models here.
class contactform(forms.ModelForm):  
	name=forms.CharField(max_length=200)
	mobile=forms.CharField(max_length=200)
	email=forms.CharField(max_length=200)
	subject=forms.CharField(max_length=200)
	message=forms.CharField(max_length=200)
	class Meta:
		model=contact
		fields="__all__"
		
class registrationform(forms.ModelForm):  
	name=forms.CharField(max_length=200)
	fathername=forms.CharField(max_length=200)
	mothername=forms.CharField(max_length=200)
	gender=forms.CharField(max_length=200)
	contactno=forms.CharField(max_length=200)
	dateofbirth=forms.CharField(max_length=200)
	address=forms.CharField(max_length=200)
	qualification=forms.CharField(max_length=200)
	stream=forms.CharField(max_length=200)
	course=forms.CharField(max_length=200)
	prefferedtime=forms.CharField(max_length=200)
	registrationdate=forms.CharField(max_length=200)
	class Meta:
		model=registration
		fields="__all__"
		
class FAQsform(forms.ModelForm):  
	question=forms.CharField(max_length=200)
	answer=forms.CharField(max_length=900)
	class Meta:
		model=contact
		fields="__all__"
		
		

class coursesform(forms.ModelForm):  
	name=forms.CharField(max_length=200)
	description=forms.CharField(max_length=900)
	eligibility=forms.CharField(max_length=200)
	fees=forms.CharField(max_length=200)
	timing=forms.CharField(max_length=200)
	class Meta:
		model=courses
		fields="__all__"
		
		
class studymaterialform(forms.ModelForm):
	booktitle=forms.CharField(max_length=255)
	photo=forms.CharField(max_length=255)
	link=forms.CharField(max_length=300)
	class Meta:
		model=studymaterial
		fields="__all__"
		
class successform(forms.ModelForm):
	photo=forms.ImageField(max_length=255)
	name=forms.CharField(max_length=255)
	rollno=forms.CharField(max_length=300)
	clearcourse=forms.CharField(max_length=300)
	class Meta:
		model=success
		fields="__all__"
		
class vacancyform(forms.ModelForm):
	companyname=forms.CharField(max_length=200)
	companylink=forms.CharField(max_length=300)
	post=forms.CharField(max_length=200)
	postlink=forms.CharField(max_length=300)
	noofvacancy=forms.CharField(max_length=20000)
	eligibility=forms.CharField(max_length=200)
	date=forms.CharField(max_length=200)
	class Meta:
		model=vacancy
		fields="__all__"
		


		