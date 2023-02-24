from django.db import models

# Create your models here.


class Inventory(models.Model):
    title = models.TextField()
    content = models.TextField()
