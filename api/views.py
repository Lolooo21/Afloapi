
from django.http import HttpRequest,HttpResponse,JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Formation
from .serializers import FormationSerializer



@api_view(['GET'])#décorateur de rest_framework pour définir la route de l'API
#cela crée une API
def home(request:HttpRequest) -> HttpResponse:
    user = {
        "name":"Laurent",
        "age":39,
    }
    return JsonResponse(user)


@api_view(['GET','POST'])#soit requete GET pour créer ou POST pour recevoir
def formations(request) -> HttpResponse:
    if request.method == "GET":
        formations = Formation.objects.all()
        #transforme les infos en JSON
        serialized_formations = FormationSerializer(formations, many=True)
        #ajouter le .data sur toutes les demandes de récupérations d'infos transformé
        return Response(serialized_formations.data)
    elif request.method == "POST":
        new_formation = FormationSerializer(data=request.data)
        if new_formation.is_valid():
            new_formation.save()
            return Response({"message": "Formation créée !"})
        else:
            return Response({"error":"mauvais body"})#si on se trompe dans les champs de création ex nom en name
    return Response()    

@api_view(['GET','PUT','DELETE'])
def formation(request,pk=int) -> HttpResponse:
    if request.method == "GET":#créer
        formation = Formation.objects.get(id=pk) 
        serialized_formation = FormationSerializer(formation, many=True)
        return Response(serialized_formation.data)
    elif request.method == "PUT":#modifier
        formation = Formation.objects.get(id=pk)
        updated_formation = FormationSerializer(instance=formation, data=request.data)
        if updated_formation.is_valid():
            updated_formation.save()
            return Response({"Message":"Formation modifiée !"})
        else:
            return Response({"error": "Mauvais body..."})
    elif request.method == "DELETE":#effacer
        formation = Formation.objects.get(id=pk)
        formation.delete()
        return Response({"message": "Formation supprimée !"})
    return Response()
    