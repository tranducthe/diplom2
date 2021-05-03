from django.db import models

# Create your models here.

class ListAreas(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    pictrure = models.ImageField(upload_to='Uni_picture')

    def __str__(self):
        return self.name


class Detailjob_view(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    pictrure = models.ImageField(upload_to='Uni_picture')

    def __str__(self):
        return self.name


