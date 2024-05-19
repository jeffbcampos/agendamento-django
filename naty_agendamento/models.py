from django.db import models

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name    
class Schedule(models.Model):
    id = models.AutoField(primary_key=True)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    hour = models.TimeField()
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.description
