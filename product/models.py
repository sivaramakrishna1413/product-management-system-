from django.db import models
from datetime import datetime

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=500)

    def __str__(self):
        return self.name


class products(models.Model):
    id=models.AutoField(primary_key=True,null=False,blank=False)
    image=models.ImageField(null=False,blank=False)
    name=models.CharField(max_length=100,null=False,blank=False)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,default=True,blank=False)
    price=models.DecimalField(max_digits=5,decimal_places=2)
    description=models.TextField()
    is_publish=models.BooleanField(default=True)
    created_at=models.DateTimeField(default=datetime.now,blank=False)

    def __str__(self):
        return self.name