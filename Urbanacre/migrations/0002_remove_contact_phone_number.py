# Generated by Django 5.0.2 on 2024-03-29 07:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Urbanacre', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='phone_number',
        ),
    ]