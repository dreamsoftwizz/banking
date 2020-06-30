from django.contrib import admin
from student.models import contact,registration, FAQs,courses,studymaterial,success,vacancy
# Register your models here.

@admin.register(contact)
class contactAdmin(admin.ModelAdmin):
	list_display=('name','mobile','email','subject','message',)
	
@admin.register(registration)
class registrationAdmin(admin.ModelAdmin):
	list_display=('name','fathername','mothername','gender','contactno','dateofbirth','address','qualification','stream','course','prefferedtime','registrationdate',)
	
@admin.register(FAQs)
class FAQsAdmin(admin.ModelAdmin):
	pass
	

	
@admin.register(courses)
class coursesAdmin(admin.ModelAdmin):
	pass
	
@admin.register(studymaterial)
class studymaterialAdmin(admin.ModelAdmin):
	pass
	
@admin.register(success)
class successAdmin(admin.ModelAdmin):
	pass
	
@admin.register(vacancy)
class vacancyAdmin(admin.ModelAdmin):
	pass

	