from django.db import models
# Create your models here.
class CRUD(models.Model):
    Image=models.ImageField(upload_to='image')
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=250)
    price=models.IntegerField()