from django.db import models

class Com(models.Model):
    title = models.CharField(max_length=128)
    link = models.URLField(max_length=200)
    year = models.IntegerField(choices=[
        (2022, '2022'),
        (2023, '2023'),
        (2024, '2024'),
    ])

    def get_image(self):
        # Define la ruta de la imagen asociada a cada año dentro de la subcarpeta "assets" en "static"
        images = {
            2022: 'assets/com22.jpg',
            2023: 'assets/com23.jpg',
            2024: 'assets/vinyl.png',
        }
        return images.get(self.year, 'assets/default.jpg')  # Ruta por defecto si el año no coincide

    def __str__(self):
        return f"{self.title}, {self.year}"

class Web(models.Model):
    title = models.CharField(max_length=128)
    link = models.URLField(max_length=200)

    def __str__(self):
        return self.title
    
class Data(models.Model):
    title = models.CharField(max_length=128)
    link = models.URLField(max_length=200)

    def __str__(self):
        return self.title

class Curriculum(models.Model):
    title = models.CharField(max_length=200)
    pdf = models.FileField(upload_to='pdfs/')  # Almacena los archivos PDF en la carpeta 'pdfs' dentro de 'MEDIA_ROOT'

    def __str__(self):
        return self.title