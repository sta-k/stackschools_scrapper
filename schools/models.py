from django.db import models

# Create your models here.
class School(models.Model):
    code = models.IntegerField(default=1000000) # 7 digit integer
    html = models.TextField()

    def __str__(self) -> str:
        resp = f'{self.code}'
        if self.html == 'no data':
            resp += '(empty)'
        return resp

class CeleryTasks(models.Model):
    started = models.DateTimeField()
    finished = models.DateTimeField(null=True, blank=True)
    name = models.CharField(max_length=200)
    def __str__(self) -> str:
        end = self.finished.strftime('%Y-%m-%d %H:%M:%S%z') if self.finished else ''
        return f'{self.name} {self.started:%Y-%m-%d %H:%M:%S%z} to {end}'