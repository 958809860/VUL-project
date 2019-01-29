from django.db import models

# Create your models here.

class Questions(models.Model):
    id = models.AutoField(primary_key = True)
    questionConttent = models.CharField(max_length = 200,unique = True)
    answer = models.CharField(max_length = 50)
