from django.db import models
from django.conf import settings

class Equipament(models.Model):
    name = models.CharField(max_length=150)
    image = models.TextField()
    description = models.CharField(max_length=500)
    active = models.BooleanField(default=True)

class Equipaments_Comment(models.Model):
    comment = models.CharField(max_length=500)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user_id', on_delete=models.CASCADE, blank=False)
    equipament_id = models.ForeignKey(Equipament, related_name='requipament_id', on_delete=models.CASCADE, blank=False)
    create_date =  models.DateField(auto_now_add=True)