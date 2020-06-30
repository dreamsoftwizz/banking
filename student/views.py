from django.shortcuts import render,redirect

from student.models import contact,registration, FAQs, courses, studymaterial,success, vacancy
from student.forms import contactform,registrationform, FAQsform, coursesform, studymaterialform,successform, vacancyform


from django.views.generic import TemplateView,ListView
# Create your views here.
def showhome(request):
    successstar = success.objects.all().order_by('-id')[:4]
    
    context = {
        'successstar': successstar,
        
    }
    return render(request, "home.html", context)

class aboutpageview(TemplateView):
	template_name="about.html"
class coursespageview(TemplateView):
	template_name="courses.html"
class ibpspageview(TemplateView):
	template_name="ibps.html"
class successstoriespageview(TemplateView):
	template_name="successstories.html"
class contactpageview(TemplateView):
	template_name="contact.html"
class registrationpageview(TemplateView):
	template_name="registration.html"
	
class videopageview(TemplateView):
	template_name="video.html"
class FAQspageview(ListView):
	template_name="FAQs.html"
	def get_queryset(self):
		return FAQs.objects.all()

class coursespageview(ListView):
	template_name="courses.html"
	def get_queryset(self):
		return courses.objects.all()
class studymaterialpageview(ListView):
	template_name="studymaterial.html"
	def get_queryset(self):
		return studymaterial.objects.all()
class successpageview(ListView):
	template_name="success.html"
	def get_queryset(self):
		return success.objects.all()
class vacancypageview(ListView):
	template_name="vacancy.html"
	def get_queryset(self):
		return vacancy.objects.all()

	
def insert(request):
	if request.method=='POST':
		form=contactform(request.POST)
		if form.is_valid():
			try:
				form.save()
				return redirect('/contact/')
			except:
				pass
	else:
		form=contactform()
	return render(request,'contact.html',{'form':form})
	

	
def insert1(request):
	if request.method=='POST':
		form=registrationform(request.POST)
		if form.is_valid():
			try:
				form.save()
				return redirect('/paytm/')
			except:
				pass
	else:
		form=registrationform()
	return render(request,'registration.html',{'form':form})

