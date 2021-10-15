from django.db import models

# Create your models here.
class School(models.Model):
    code = models.IntegerField(default=1000000) # 7 digit integer
    html = models.TextField()