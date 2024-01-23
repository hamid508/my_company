from django.contrib import admin
from .models import Company_Details, Service, Testimonial, Job, Technology

# Register your models here.
admin.site.register(Company_Details)
admin.site.register(Service)
admin.site.register(Testimonial)
admin.site.register(Technology)
admin.site.register(Job)
