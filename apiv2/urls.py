from rest_framework import routers
from .views import UtilisateurViewSet, UtilisatriceViewSet


router = routers.DefaultRouter()
router.register('utilisateurs', UtilisateurViewSet)
router.register('utilisatrice', UtilisatriceViewSet)#(nom de la route + nsysteme de views)


