from rest_framework.generics import ListCreateAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Song
from .serializers import SongSerializer


class SongView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Song.objects.all()
    serializer_class = SongSerializer

    def perform_create(self, serializer):
        serializer.save(album_id=self.kwargs['pk'])
