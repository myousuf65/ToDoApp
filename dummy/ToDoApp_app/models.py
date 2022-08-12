from django.db import models

# Create your models here.
class ToDoApp_model(models.Model):
    item = models.CharField(max_length=200)

    def __str__(self):
        return self.item