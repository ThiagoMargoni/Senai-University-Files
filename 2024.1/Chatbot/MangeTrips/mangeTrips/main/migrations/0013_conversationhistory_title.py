# Generated by Django 4.2.5 on 2024-03-18 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_conversationhistory_lastcommand'),
    ]

    operations = [
        migrations.AddField(
            model_name='conversationhistory',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
