# Generated by Django 5.2 on 2025-04-13 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0020_alter_com_title_alter_com_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='com',
            name='title',
            field=models.CharField(max_length=128),
        ),
    ]
