from django.db import models

# Create your models here.
class School(models.Model):
    code = models.IntegerField(default=1000000) # 7 digit integer
    html = models.TextField()

    def __str__(self) -> str:
        return self.code

class CeleryTasks(models.Model):
    started = models.DateTimeField()
    finished = models.DateTimeField(null=True, blank=True)
    name = models.CharField(max_length=200)
    def __str__(self) -> str:
        return f'{self.name} {self.started} to {self.finished}'