from rest_framework import serializers
from .models import (
    Artist, Album, Track,
    Genre, MediaType,
    Playlist, PlaylistTrack
)


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = "__all__"

class AlbumSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer(read_only=True)

    class Meta:
        model = Album
        fields = "__all__"

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"

class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = "__all__"
        
class MediaTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaType
        fields = "__all__"
class TrackSerializer(serializers.ModelSerializer):
    album = AlbumSerializer(read_only=True)
    genre = GenreSerializer(read_only=True)
    media_type = MediaTypeSerializer(read_only=True)

    class Meta:
        model = Track
        fields = "__all__"