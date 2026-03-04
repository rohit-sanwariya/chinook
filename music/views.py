from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *


class ArtistViewSet(ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class AlbumViewSet(ModelViewSet):
    queryset = Album.objects.select_related("artist").all()
    serializer_class = AlbumSerializer


class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class MediaTypeViewSet(ModelViewSet):
    queryset = MediaType.objects.all()
    serializer_class = MediaTypeSerializer


class PlaylistViewSet(ModelViewSet):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer


class TrackViewSet(ModelViewSet):
    queryset = (
        Track.objects
        .select_related("album", "genre", "media_type")
        .prefetch_related("playlists")
        .all()
    )
    serializer_class = TrackSerializer