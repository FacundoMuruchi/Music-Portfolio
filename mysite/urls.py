from django.urls import path
from .views import resume, projects, contact

urlpatterns = [
    path('resume/', resume, name='resume'),
    path('projects/', projects, name='projects'),
    path('contact/', contact, name='contact'),
]