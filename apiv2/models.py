from django.db import models

# Create your models here.
class Utilisateur(models.Model):
    nom=models.CharField(max_length=30)
    age=models.IntegerField()
    is_admin=models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.nom}"
    

class Utilisatrice(models.Model):
    nom=models.CharField(max_length=30)
    age=models.IntegerField()
    is_free=models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.nom}"