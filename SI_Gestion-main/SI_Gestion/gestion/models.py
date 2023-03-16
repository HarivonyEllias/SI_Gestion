from django.db import models

# Create your models here.
class Infosociete(models.Model):
    idsociete=models.AutoField(primary_key=True)
    nom = models.CharField(max_length=255)
    objet = models.CharField(max_length=255)
    siege = models.CharField(max_length=255)
    adresse_exploitation = models.CharField(max_length=255)
    dirigeant = models.CharField(max_length=255)
    date_creation = models.DateField()
    identite_fiscale = models.CharField(max_length=255)
    numero_statistique = models.CharField(max_length=255)
    numero_registre_commerce = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    devise_compte = models.CharField(max_length=255)
    
    class Meta:
        managed=False
        db_table = 'infosociete' 

class CountSociete(models.Model):
    idcount_societe=models.AutoField(primary_key=True)
    idsociete=models.IntegerField()
    mot_de_passe = models.CharField(max_length=100)
    
    class Meta:
        managed=False
        db_table = 'count_societe' 
