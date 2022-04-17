from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

# Create your models here.
class MainMenu(models.Model):
    Alias = models.CharField(max_length=255, null=True)
    Name = models.CharField(max_length=20, null=True)
    Position = models.IntegerField(null=True)

    def __str__(self):
        return self.Name



#Добавляем в админку

admin.site.register(MainMenu)