from rest_framework.serializers import ModelSerializer
from .models import Utilisateur, Utilisatrice


class UtilisateurSerializer(ModelSerializer):
    class Meta:
        model=Utilisateur
        fields="__all__"

class UtilisatriceSerializer(ModelSerializer):
    class Meta:
        model=Utilisatrice
        fields="__all__"        