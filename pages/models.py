from django.db import models

class ProductManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()
class Pages(models.Model):
    title=models.CharField(max_length=255)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    img=models.ImageField(upload_to='photos/%Y/%m/%d',null=True,blank=True)
    description=models.TextField(blank=True)

    def __str__(self):
        return self.title
