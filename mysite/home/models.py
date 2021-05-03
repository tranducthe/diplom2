from django.db import models

# Create your models here.

class ListUni(models.Model):
    name = models.CharField(max_length=100)
    anddress = models.CharField(max_length=200)
    description = models.TextField()
    excerpt = models.TextField(max_length=300)
    pictrure = models.ImageField(upload_to='Uni_picture')

    def __str__(self):
        return self.name


