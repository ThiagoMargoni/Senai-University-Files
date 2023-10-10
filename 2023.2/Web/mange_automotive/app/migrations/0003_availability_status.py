# Generated by Django 4.2.5 on 2023-10-10 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_availability_status_maintenance_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='availability',
            name='status',
            field=models.CharField(choices=[('A', 'Available'), ('U', 'Unavailable')], default='A', max_length=100),
        ),
    ]