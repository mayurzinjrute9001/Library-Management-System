from django.db import models

class Library_User(models.Model):
    name=models.CharField(max_length=25)
    email=models.EmailField(max_length=25)
    password=models.CharField(max_length=25)

    def __str__(self):
        return self.name