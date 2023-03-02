from django.db import models

# Create your models here.

class Prints(models.Model):
    name=models.CharField(max_length=50)
    phone=models.CharField(max_length=10)
    email=models.CharField(max_length=254)
    desc=models.TextField()
    pdf=models.FileField( upload_to=None, max_length=100)
    freq=models.IntegerField()
    spiral=models.BooleanField()
    date=models.DateField()


    def __str__(self):
        #to name the model by the name
        return self.name
    