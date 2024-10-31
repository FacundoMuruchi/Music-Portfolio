from django.db import models

class Com(models.Model):
    GENRE_CHOICES = [
        ('Rock', 'Rock'),
        ('Jazz', 'Jazz'),
        ('Pop', 'Pop'),
        ('Orchestral', 'Orchestral'),
    ]

    title = models.CharField(max_length=128)
    preview = models.FileField(upload_to='previews/', blank=True, null=True)
    year = models.IntegerField(choices=[
        (2022, '2022'),
        (2023, '2023'),
        (2024, '2024'),
    ])

    version = models.CharField(max_length=128, choices=[
        ('Original', 'Original'),
        ('Remake', 'Remake'),
        ('Alternative Version', 'Alternative Version'),
    ], blank=True, null=True)

    genre = models.CharField(max_length=32, choices=GENRE_CHOICES, default='Pop')  # Campo para el género de la canción

    def get_image(self):
        # Define la ruta de la imagen asociada a cada año dentro de la subcarpeta "assets" en "static"
        images = {
            2022: 'assets/com22.jpg',
            2023: 'assets/com23.jpg',
            2024: 'assets/vinyl.png',
        }
        return images.get(self.year, 'assets/default.jpg')  # Ruta por defecto si el año no coincide

    def __str__(self):
        return f"{self.title}, {self.year}, {self.genre}"