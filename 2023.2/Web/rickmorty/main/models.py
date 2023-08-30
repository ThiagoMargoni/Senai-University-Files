from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=150)
    type = models.CharField(max_length=100)
    dimension = models.CharField(max_length=100)
    residents = models.TextField()
    url = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Episode(models.Model):
    name = models.CharField(max_length=150)
    air_date = models.DateTimeField()
    episode = models.CharField(max_length=150)
    characters = models.TextField()
    url = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Character(models.Model):
    ALL_STATUS = [
        ('Dead', 'Dead'),
        ('Unknown', 'Unknown'),
        ('Alive', 'Alive'),
    ]

    GENDERS = [
        ('Female', 'Female'), 
        ('Male', 'Male'), 
        ('Genderless', 'Genderless'), 
        ('Unknown', 'Unknown'), 
    ]

    name = models.CharField(max_length=150)
    status = models.CharField(max_length=10, choices=ALL_STATUS, default='Unknown')
    species = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=GENDERS, default='Unknown')
    origin = models.ForeignKey('Location', related_name='origin', on_delete=models.CASCADE, null=True)
    location = models.ForeignKey('Location', related_name='location', on_delete=models.CASCADE, null=True)
    image = models.TextField()
    episodes = models.TextField()
    url = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name