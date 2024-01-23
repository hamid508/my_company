from django.shortcuts import render, HttpResponse, redirect, reverse
from .models import Service, Testimonial, Job, Technology, Company_Details
from . import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required



def Home(request):
    testimonials= Testimonial.objects.all()
    technology= Technology.objects.all()
    company_details=Company_Details.objects.all()
    
    my_dict={ 
            'testimonials': testimonials,
            'technology': technology, 
            'company_details':company_details,
            }
    return render (request, 'company/home.html', my_dict)

def About(request):
    technology= Technology.objects.all()
    company_details=Company_Details.objects.all()
    services= Service.objects.all()
    my_dict={ 
            'technology': technology, 
            'company_details':company_details,
            'services': services,
            }
    return render (request, 'company/about.html', my_dict)

def Contact(request):
    technology= Technology.objects.all()
    company_details=Company_Details.objects.all()
    services= Service.objects.all()
    my_dict={ 
            'technology': technology, 
            'company_details':company_details,
            'services': services,
            }
    return render (request, 'company/contact.html',my_dict)

def OurServices(request):
    technology= Technology.objects.all()
    company_details=Company_Details.objects.all()
    services= Service.objects.all()
    my_dict={ 
            'technology': technology, 
            'company_details':company_details,
            'services': services,
            }
    return render (request, 'company/our-services.html',my_dict)

def ServiceDetail(request, url):
    servicedetail= Service.objects.get(url=url)
    print(servicedetail)  
    technology= Technology.objects.all()
    company_details=Company_Details.objects.all()
    services= Service.objects.all()
    my_dict={ 
            'technology': technology, 
            'company_details':company_details,
            'services': services,
            }
    return render(request, 'company/service-detail.html', {'servicedetail': servicedetail} ,my_dict)

# def TechnologyDetail(request, url):
#     technologydetail= Technology.objects.get(url=url)
#     print(technologydetail)  
#     return render(request, 'company/technology-detail.html', {'technologydetail': technologydetail})

def jobsHome(request):
    all_jobs= models.Job.objects.all()
    technology= Technology.objects.all()
    company_details=Company_Details.objects.all()
    services= Service.objects.all()
    my_dict={ 
            'technology': technology, 
            'company_details':company_details,
            'services': services,
            'all_jobs':all_jobs,
            }
    return render (request, 'company/jobsHome.html',my_dict )

@login_required(login_url='sign-in')
def add_job(request):
    if (request.POST):
        title=request.POST['title']     
        company= request.POST['company']
        pay= request.POST['pay']
        job_type= request.POST['job_type']
        location= request.POST['location']
        application_deadline= request.POST['application_deadline']
        job_discription= request.POST['job_discription']
        positions= request.POST['positions']
        models.Job.objects.create(
            title= title, 
            company= company, 
            pay= pay, 
            job_type= job_type, 
            location= location, 
            application_deadline= application_deadline, 
            job_discription= job_discription,  
            positions= positions,
            )
        return render(request, 'company/jobsHome.html')    
    else:
        return render(request, 'company/add-new-job.html')
    
# user authentication Login and register
@login_required(login_url='sign-in')
def Account(request):
    return render(request,'company/account.html' )  

def sign_in(request):
    if request.method == 'POST':
        username= request.POST.get('username')
        pass1= request.POST.get('pass1')
        user= authenticate(request, username= username, password= pass1)
        if user is not None:
            login(request, user)
            return redirect(Home)
        else:
            return HttpResponse(" <h3>Username or Password is incorrect! Try again</h3>")
    
    return render (request, 'company/sign-in.html')

def sign_up(request):
    if request.method == 'POST':
        name= request.POST.get('Name')
        username= request.POST.get('username')
        email= request.POST.get('email')
        password= request.POST.get('pass1')
        pass2= request.POST.get('pass2')
        if password!= pass2:
            return HttpResponse("Your password does'nt match")
        else:       
         new_user = User.objects.create_user(username, email,  password )
         new_user.save()     
         return redirect('sign-in')
    
    return render (request, 'company/sign-up.html')
    
def sign_out(request):
     logout(request)
     return redirect('sign-in')