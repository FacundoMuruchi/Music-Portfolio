from django.shortcuts import render
from django.db.models import Q

from django.core.paginator import EmptyPage, PageNotAnInteger
from .models import Com

from django.views.generic import ListView

# Create your views here.
def projects(request):
    return render(
        request=request,
        template_name='mysite/projects.html'
    )

def contact(request):
    return render(
        request=request,
        template_name='mysite/contact.html'
    )

def coms(request):
    return render(
        request=request,
        template_name='mysite/coms/coms.html'
    )

class PostListView(ListView):
    model = Com
    template_name = "mysite/coms/coms-list.html"
    context_object_name = 'object_list'
    paginate_by = 6

    def get_queryset(self):
        year = self.kwargs.get('year')
        genre = self.request.GET.get('genre', '')
        queryset = Com.objects.filter(year=year)
        if genre:
            queryset = queryset.filter(genre=genre)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['year'] = self.kwargs.get('year')
        context['selected_genre'] = self.request.GET.get('genre', '')
        # Agrega la lista de géneros al contexto
        context['genres'] = Com.GENRE_CHOICES
        return context