from django.db import models

# Create your models here.
class product(models.Model):
    id = models.AutoField(primary_key=True)
    product_id = models.PositiveIntegerField(null=False)
    name = models.CharField(max_length=20,null=False)
    desc = models.CharField(max_length=50,null=False)
    remark = models.CharField(max_length=50)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

class downloadlink(models.Model):
    id = models.AutoField(primary_key=True)
    link_id = models.PositiveIntegerField(null=False)
    product_id = models.PositiveIntegerField(null=False)
    product_link = models.CharField(max_length=10000,null=False)