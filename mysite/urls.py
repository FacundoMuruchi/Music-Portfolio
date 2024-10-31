from django.urls import path
from .views import projects, contact, coms, PostListView

urlpatterns = [
    path('projects/', projects, name='projects'),
    path('contact/', contact, name='contact'),
    path('commisions/', coms, name='coms'),
    path('commissions-list/<int:year>/', PostListView.as_view(), name='coms-list'),
]