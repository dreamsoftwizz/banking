from django.db import models

# Create your models here.
class contact(models.Model):
	name=models.CharField(max_length=200)
	mobile=models.CharField(max_length=200)
	email=models.CharField(max_length=200)
	subject=models.CharField(max_length=200)
	message=models.CharField(max_length=200)
	class Meta:
		db_table="contact"
	def __str__(self):
		return self.name
		
class registration(models.Model):
	name=models.CharField(max_length=200)
	fathername=models.CharField(max_length=200, default="")
	mothername=models.CharField(max_length=200, default="")
	gender=models.CharField(max_length=200, default="")
	contactno=models.CharField(max_length=200, default="")
	dateofbirth=models.CharField(max_length=200,default="")
	address=models.CharField(max_length=200, default="")
	qualification=models.CharField(max_length=200)
	stream=models.CharField(max_length=200, default="")
	course=models.CharField(max_length=200)
	prefferedtime=models.CharField(max_length=200, default="")
	registrationdate=models.CharField(max_length=200, default="")
	class Meta:
		db_table="registration"
	def __str__(self):
		return self.name
		
class FAQs(models.Model):
	question=models.CharField(max_length=200)
	answer=models.CharField(max_length=900, default="")
	class Meta:
		db_table="FAQs"
	def __str__(self):
		return self.question
		

		
class courses(models.Model):
	name=models.CharField(max_length=200)
	description=models.CharField(max_length=900, default="")
	eligibility=models.CharField(max_length=200)
	fees=models.CharField(max_length=200)
	timing=models.CharField(max_length=200)
	class Meta:
		db_table="courses"
	def __str__(self):
		return self.name
		
class studymaterial(models.Model):
	booktitle=models.CharField(max_length=255)
	photo=models.ImageField(upload_to='images/')
	link=models.CharField(max_length=300)
	class Meta:
		db_table="studymaterial"
	def __str__(self):
		return self.booktitle
		
class success(models.Model):
	photo=models.ImageField(upload_to='images/')
	name=models.CharField(max_length=255)
	rollno=models.CharField(max_length=300)
	clearcourse=models.CharField(max_length=300)
	class Meta:
		db_table="success"
	def __str__(self):
		return self.name
		
class vacancy(models.Model):
	companyname=models.CharField(max_length=200)
	companylink=models.CharField(max_length=300, default="")
	post=models.CharField(max_length=200)
	postlink=models.CharField(max_length=300, default="")
	noofvacancy=models.CharField(max_length=200)
	eligibility=models.CharField(max_length=200)
	date=models.CharField(max_length=200)
	class Meta:
		db_table="vacancy"
	def __str__(self):
		return self.companyname

