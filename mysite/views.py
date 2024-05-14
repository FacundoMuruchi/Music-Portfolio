from django.shortcuts import render

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