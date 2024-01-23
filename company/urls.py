from django.urls import path
from. import views

urlpatterns = [
    path('', views.Home, name='home'),   
    path('about/', views.About, name='about'),   
    path('contact/', views.Contact, name='contact'),   
    path('sign-up/', views.sign_up, name='sign-up'),   
    path('sign-in/', views.sign_in, name='sign-in'),   
    path('sign-out/', views.sign_out, name='sign-out'),   
    path('account/', views.Account, name='account'),   
    path('our-services/', views.OurServices, name='OurServices'),   
    path('our-services/<slug:url>/', views.ServiceDetail, name='ServiceDetail'),   
    # path('/<slug:url>/', views.TechnologyDetail, name='TechnologyDetail'),   
    path('jobs/', views.jobsHome, name='jobs'),
    path('add-new-job/', views.add_job, name='AddJob'),
    
    
    ]
