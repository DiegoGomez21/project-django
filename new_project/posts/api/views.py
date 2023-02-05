from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from posts.models import Post



class PostApiView(APIView):
    #Vamos a usar la ORM para traer datos de la base de datos
    def get(self, request):
        #posts = Post.objects.all() #Si lo envío asi, me peta el servidor, por eso se hace necesario serializar los datos
        posts = [a.title for a in Post.objects.all()]
        return Response(status=status.HTTP_200_OK, data=posts)

    #End-point con metodo post

    def post(self, request):
        Post.objects.create(title=request.POST['title'], description=request.POST['description'], order=request.POST['order'])
        return self.get(request)