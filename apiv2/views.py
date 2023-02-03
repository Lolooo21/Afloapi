from rest_framework.viewsets import ModelViewSet
from .models import Utilisateur,Utilisatrice
from .serializers import UtilisateurSerializer,UtilisatriceSerializer
# Create your views here.

class UtilisateurViewSet(ModelViewSet):
    queryset = Utilisateur.objects.all()
    serializer_class = UtilisateurSerializer
    filterset_fields = ['is_admin']   
    search_fields = ['nom'] 

class UtilisatriceViewSet(ModelViewSet):
    queryset = Utilisatrice.objects.all()
    serializer_class = UtilisatriceSerializer
    filterset_fields = ['is_free']   
    search_fields = ['nom'] 