# Generated by Django 4.2.6 on 2024-07-16 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0013_delete_curriculum'),
    ]

    operations = [
        migrations.AddField(
            model_name='com',
            name='version',
            field=models.IntegerField(blank=True, choices=[('original', 'Original'), ('remake', 'Remake'), ('alternative', 'Alternative Version')], null=True),
        ),
    ]