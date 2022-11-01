from rest_framework import viewsets, status
from api.models import *
from api.serializers import *
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def retrieve(self, request, *args, **kwargs):
        id = kwargs['pk']
        if(id.isnumeric()==False):
            user = get_object_or_404(User, username=id)
            serializer = self.serializer_class(user).data
            return Response(serializer)
        return super().retrieve(request, *args, **kwargs)
    
    def create(self, request, *args, **kwargs):
        try:
            serializer = LivroSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            
            # ADDING NEW LIVROS IN USER.LIVROS ARRAY
            id = request.data.get('user')
            pk = serializer.data['id']
            if(isinstance(id, int)):
                user = get_object_or_404(User, pk=id)
            else:
                user = get_object_or_404(User, username=id)
            
            livro = get_object_or_404(Livro, pk=pk)
            user.livros.add(livro)
            user.save()
            serializer = self.serializer_class(user).data

            return Response(serializer)
            
        except:
            return super().create(request, *args, **kwargs) 
    
    
class LivroViewSet(viewsets.ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer

class PseudoAuthentication(APIView):
    def post(self, request):
        try:
            username = request.data.get('username')
            password = request.data.get('password')
            user = User.objects.get(username=username, password=password)
            return Response(
                {
                    "STATUS_CODE": status.HTTP_202_ACCEPTED,
                    "STATUS": "AUTHORIZED"
                }
            )
        except:
            return Response(
                {
                    "STATUS_CODE": status.HTTP_401_UNAUTHORIZED,
                    "STATUS": "UNAUTHORIZED"
                }
            )

        
            
            
        
        
    
    
              

        
