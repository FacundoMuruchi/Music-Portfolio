import os
from datetime import datetime
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
    year = models.IntegerField(default=datetime.now().year)
    version = models.CharField(max_length=128, choices=[
        ('Original', 'Original'),
        ('Remake', 'Remake'),
        ('Alternative Version', 'Alternative Version'),
    ], blank=True, null=True)
    genre = models.CharField(max_length=32, choices=GENRE_CHOICES, default='Pop')

    def save(self, *args, **kwargs):
        # Solo autocompleta el título si no ha sido proporcionado manualmente
        if self.preview and not self.title:
            filename = os.path.basename(self.preview.name)
            name, _ = os.path.splitext(filename)
            self.title = name
        super().save(*args, **kwargs)

    def get_image(self):
        images = {
            2022: 'assets/com22.jpg',
            2023: 'assets/com23.jpg',
            2024: 'assets/vinyl.png',
            2025: 'assets/com25.jpg',
        }
        return images.get(self.year, 'assets/default.jpg')

    def __str__(self):
        return f"{self.title}, {self.year}, {self.genre}"
