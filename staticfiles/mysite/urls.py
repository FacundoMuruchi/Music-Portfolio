from django.urls import path
from .views import resume, projects, contact, download_cv, coms, PostListView, PostListViewWebs, PostListViewDatas

urlpatterns = [
    path('resume/', resume, name='resume'),
    path('projects/', projects, name='projects'),
    path('contact/', contact, name='contact'),
    path('download/', download_cv, name='download'),
    path('commisions/', coms, name='coms'),
    path('commissions-list/<int:year>/', PostListView.as_view(), name='coms-list'),
    path('web-sites/', PostListViewWebs.as_view(), name='websites'),
    path('notebooks/', PostListViewDatas.as_view(), name='notebooks'),
]