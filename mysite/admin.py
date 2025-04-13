from django.contrib import admin
from .models import Com

# Register your models here.

@admin.register(Com)
class ComAdmin(admin.ModelAdmin):
    exclude = ('title', 'year')