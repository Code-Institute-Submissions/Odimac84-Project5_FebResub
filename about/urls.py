from django.urls import path
from . import views

urlpatterns = [
    path('', views.about_view , name='about'),
    path('contact', views.contact_view , name='contact'),
    path('create_contact', views.create_contact , name='create_contact'),
    path('create_testimonial', views.create_testimonial , name='create_testimonial'),
]
