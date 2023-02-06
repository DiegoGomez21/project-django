from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework import status
from posts.models import Post
from posts.api.serializers import PostSerializer
from posts.api.permissions import IdAdminOrReadOnly


#De esta manera ya tenemos el CRUD completo
class PostModelViewSet(ModelViewSet):
    permission_classes=[IdAdminOrReadOnly] 
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    #Puedo elegir que solo nos muestre y nos permita un método
    http_method_names=['get']
    #Vamos a ver el tema de los permisos
    
    





# #Usando viewset se hace necesario definir un sistema de rutas
# class PostViewSet(ViewSet):
#     #Vamos a usar la ORM para traer datos de la base de datos
#     def list(self, request):
#         #posts = Post.objects.all() #Si lo envío asi, me peta el servidor, por eso se hace necesario serializar los datos
#         serializer = PostSerializer(Post.objects.all(), many=True)
#         return Response(status=status.HTTP_200_OK, data=serializer.data)

#     #End-point con metodo post

#     def retrieve(self, request, pk: int):
#         post = PostSerializer(Post.objects.get(pk=pk))
#         return Response(status=status.HTTP_200_OK, data=post.data)
    
#     def create(self, request):
#         serializer = PostSerializer(data=request.POST)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response( status=status.HTTP_200_OK, data=serializer.data )



# class PostApiView(APIView):
#     #Vamos a usar la ORM para traer datos de la base de datos
#     def get(self, request):
#         #posts = Post.objects.all() #Si lo envío asi, me peta el servidor, por eso se hace necesario serializar los datos
#         serializer = PostSerializer(Post.objects.all(), many=True)
#         return Response(status=status.HTTP_200_OK, data=serializer.data)

#     #End-point con metodo post

#     def post(self, request):
#         serializer = PostSerializer(data=request.POST)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response( status=status.HTTP_200_OK, data=serializer.data )