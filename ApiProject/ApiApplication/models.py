from django.db import models

# Create your models here.
class Book(models.Model):
    id=models.IntegerField(primary_key=True)
    title=models.CharField(max_length=200)
    author=models.CharField(max_length=200)

def productFile(instance, filename):
    return '/'.join( ['products', str(instance.id), filename] )

class News(models.Model):
    id=models.IntegerField(primary_key=True)
    title=models.CharField(max_length=200)
    description=models.CharField(max_length=200)
    content=models.CharField(max_length=2000)





class Person(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=200)
    age=models.IntegerField()
    email=models.CharField(max_length=2000)
    password=models.CharField(max_length=32)
                