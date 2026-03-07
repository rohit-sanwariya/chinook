from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register("artists", ArtistViewSet)
router.register("albums", AlbumViewSet)
router.register("tracks", TrackViewSet)
router.register("genres", GenreViewSet)
router.register("media-types", MediaTypeViewSet)
router.register("playlists", PlaylistViewSet)

urlpatterns = router.urls