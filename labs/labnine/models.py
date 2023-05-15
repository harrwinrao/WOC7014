from django.db import models

# Create your models here.


class Game(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    developer = models.CharField(max_length=255)
    platform = models.CharField(max_length=255)

    def __str__(self):
        return self.title
