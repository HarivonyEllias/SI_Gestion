from django.db import models

# Create your models here.
class Account (models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'accounts'