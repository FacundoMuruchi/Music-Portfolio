# Generated by Django 4.2.6 on 2024-05-19 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0009_com_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='com',
            name='link',
            field=models.URLField(),
        ),
    ]
