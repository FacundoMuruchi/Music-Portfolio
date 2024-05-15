from django.shortcuts import render
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

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

def generate_pdf(request):
    # Creamos un objeto HttpResponse con el tipo de contenido pdf
    response = HttpResponse(content_type='application/pdf')
    # Especificamos el nombre del archivo como adjunto
    response['Content-Disposition'] = 'attachment; filename="Facundo_Muruchi_Resume.pdf"'

    # Creamos el documento PDF
    p = canvas.Canvas(response)

    # Obtener el tamaño de la página
    width, height = letter

    # Calcular la coordenada y de la esquina superior izquierda
    y_top_left = height

    # Dibujar el texto en la esquina superior izquierda
    p.drawString(40, y_top_left, "Este es mi currículum")
    # Cerramos el objeto Canvas
    p.showPage()
    p.save()

    return response
