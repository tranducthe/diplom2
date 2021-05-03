from django.db import models

# Create your models here.
class user(models.Model):
    name = models.CharField(max_length=100)
    anddress = models.CharField(max_length=200)
    description = models.TextField()
    excerpt = models.TextField(max_length=300)
    pictrure = models.ImageField(upload_to='Uni_picture')
    majors = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class usersST(models.Model):
    IdUser = models.IntegerField
    nameUser = models.CharField(max_length=100)

    def __str__(self):
        return self.nameUser

class usersLike(models.Model):
    IdLike = models.IntegerField
    nameLike = models.CharField(max_length=100)

    def __str__(self):
        return self.nameLike

class Career(models.Model):
    IdCareer = models.IntegerField
    nameCareer = models.CharField(max_length=100)

    def __str__(self):
        return self.nameCareer