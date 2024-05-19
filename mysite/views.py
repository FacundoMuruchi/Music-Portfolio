from django.shortcuts import render, get_object_or_404
from django.http import FileResponse

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Com, Web, Curriculum

from django.views.generic import ListView

# Create your views here.
def resume(request):
    return render(
        request=request,
        template_name='mysite/resume.html'
    )

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
    paginate_by = 6  # Muestra 6 proyectos por página

    def get_queryset(self):
        year = self.kwargs.get('year')  # Obtiene el año desde los parámetros de la URL
        return Com.objects.filter(year=year)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['year'] = self.kwargs.get('year')  # Añade el año al contexto
        paginator = context['paginator']
        page = self.request.GET.get('page')
        
        try:
            # Intenta obtener la página solicitada
            context['object_list'] = paginator.page(page)
        except PageNotAnInteger:
            # Si la página no es un número entero, devuelve la primera página.
            context['object_list'] = paginator.page(1)
        except EmptyPage:
            # Si la página está fuera de rango (p.ej. 9999), devuelve la última página de resultados.
            context['object_list'] = paginator.page(paginator.num_pages)
        return context
    
class PostListViewWebs(ListView):
    model = Web
    template_name = "mysite/webs.html"

class PostListViewDatas(ListView):
    model = Web
    template_name = "mysite/data.html"

def download_cv(request):
    curriculum = get_object_or_404(Curriculum)  # Asumiendo que solo tienes un currículum
    response = FileResponse(curriculum.pdf.open(), as_attachment=True, filename=f"{curriculum.title}.pdf")
    response['Content-Type'] = 'application/pdf'
    response['Content-Disposition'] = f'attachment; filename="{curriculum.title}.pdf"'
    return response