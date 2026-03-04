from django.contrib import admin
from .models import *

admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(Track)
admin.site.register(Genre)
admin.site.register(MediaType)
admin.site.register(Playlist)
admin.site.register(PlaylistTrack)
