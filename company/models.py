from django.db import models

# Create your models here.
class Company_Details(models.Model):
    #pk
    com_name=models.CharField(max_length=50)
    com_discription=models.CharField(max_length=200, default="")
    com_info=models.CharField(max_length=400, blank=True)
    com_logo=models.ImageField(upload_to="img/", default="")
    com_email=models.CharField(max_length=400, default="",  blank=True)
    com_location_1=models.CharField(max_length=400, default="",  blank=True)
    com_location_2=models.CharField(max_length=400, default="",  blank=True)
    com_location_3=models.CharField(max_length=400, default="",  blank=True)
    com_location_4=models.CharField(max_length=400, default="",  blank=True)
    com_phone=models.CharField(max_length=400, default="",  blank=True)
    com_facebook=models.CharField(max_length=400, default="",  blank=True)
    com_linkedin=models.CharField(max_length=400, default="",  blank=True)
    com_instagram=models.CharField(max_length=400, default="",  blank=True)
    com_slack=models.CharField(max_length=400, default="",  blank=True)
    com_skype=models.CharField(max_length=400, default="",  blank=True)
    com_youtube=models.CharField(max_length=400, default="",  blank=True)
    
    
class Service(models.Model):
    #pk
    title= models.CharField(max_length=100)
    short_disc= models.CharField(max_length=500, default="")
    content= models.CharField(max_length=2000)
    image=models.ImageField(upload_to="img/", default="")
    url= models.CharField(max_length=100, default="")
    
    def __str__(self):
        return self.title

class Technology(models.Model):
    #pk
    title= models.CharField(max_length=100)
    short_disc= models.CharField(max_length=500)
    content= models.CharField(max_length=2000)
    image=models.ImageField(upload_to="img/", default="")    
    def __str__(self):
        return self.title
        
class Testimonial(models.Model):
    #pk
    name=models.CharField(max_length=50)
    review=models.CharField(max_length=500)
    image=models.ImageField(upload_to="img/", default="")
    def __str__(self):
        return self.name
    
    
class Job(models.Model):
    #pk
    title= models.CharField(max_length=100)
    company= models.CharField(max_length=200)
    pay= models.CharField(max_length=200)
    job_type= models.CharField(max_length=200)
    location= models.CharField(max_length=500)
    job_discription= models.CharField(max_length=900)
    application_deadline= models.CharField(max_length=200)
    positions= models.CharField(max_length=200)
    
    def __str__(self):
        return self.title