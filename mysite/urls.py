from django.urls import path
from .views import resume, projects, contact, generate_pdf

urlpatterns = [
    path('resume/', resume, name='resume'),
    path('projects/', projects, name='projects'),
    path('contact/', contact, name='contact'),
    path('download/', generate_pdf, name='download'),
]