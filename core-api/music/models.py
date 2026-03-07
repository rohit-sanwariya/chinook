from django.db import models


class Artist(models.Model):
    artist_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=120, null=True, blank=True)

    class Meta:
        db_table = "artist"
        managed = False  # remove if Django should create table

    def __str__(self):
        return self.name or f"Artist {self.artist_id}"
    

class Album(models.Model):
    album_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=160)

    artist = models.ForeignKey(
        Artist,
        on_delete=models.DO_NOTHING,
        related_name="albums",
        db_column="artist_id"
    )

    class Meta:
        db_table = "album"
        managed = False

    def __str__(self):
        return self.title
    
class Genre(models.Model):
    genre_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=120, null=True, blank=True)

    class Meta:
        db_table = "genre"
        managed = False


class MediaType(models.Model):
    media_type_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=120, null=True, blank=True)

    class Meta:
        db_table = "media_type"
        managed = False

class Playlist(models.Model):
    playlist_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=120, null=True, blank=True)

    class Meta:
        db_table = "playlist"
        managed = False



class Track(models.Model):
    track_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    composer = models.CharField(max_length=220, null=True, blank=True)
    milliseconds = models.IntegerField()
    bytes = models.IntegerField(null=True, blank=True)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

    album = models.ForeignKey(
        Album,
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
        related_name="tracks",
        db_column="album_id"
    )

    media_type = models.ForeignKey(
        MediaType,
        on_delete=models.DO_NOTHING,
        related_name="tracks",
        db_column="media_type_id"
    )

    genre = models.ForeignKey(
        Genre,
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
        related_name="tracks",
        db_column="genre_id"
    )

    playlists = models.ManyToManyField(
        Playlist,
        through="PlaylistTrack",
        related_name="tracks"
    )

    class Meta:
        db_table = "track"
        managed = False

    def __str__(self):
        return self.name

class PlaylistTrack(models.Model):
    playlist = models.ForeignKey(
        Playlist,
        on_delete=models.DO_NOTHING,
        db_column="playlist_id"
    )

    track = models.ForeignKey(
        Track,
        on_delete=models.DO_NOTHING,
        db_column="track_id"
    )

    class Meta:
        db_table = "playlist_track"
        managed = False
        unique_together = ("playlist", "track")