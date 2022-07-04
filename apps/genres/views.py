from rest_framework.viewsets import ModelViewSet    
from .models import  Genre
from .serializers import GenreSerializer
from rest_framework import permissions 

class GenreViewSet(ModelViewSet):
    queryset= Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes=None
    
    
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes= [permissions.AllowAny]
        elif self.action in ['update', 'create', 'dastroy', 'partial_update']:
            self.permission_classes= [permissions.IsAdminUser]
        return [permission() for permission in self.permission_classes]


