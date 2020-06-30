from django.urls import path,include
from student import views

urlpatterns = [
path('home/',views.showhome),
path('about/',views.aboutpageview.as_view()),
path('courses/',views.coursespageview.as_view()),
path('ibps/',views.ibpspageview.as_view()),
path('successstories/',views.successstoriespageview.as_view()),
path('contact/',views.contactpageview.as_view()),
path('registration/',views.registrationpageview.as_view()),
path('FAQs/',views.FAQspageview.as_view()),
path('video/',views.videopageview.as_view()),
path('courses/',views.coursespageview.as_view()),
path('studymaterial/',views.studymaterialpageview.as_view()),
path('success/',views.successpageview.as_view()),
path('vacancy/',views.vacancypageview.as_view()),
path('insert',views.insert),
path('insert1',views.insert1),

]