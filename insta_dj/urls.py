from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularRedocView, SpectacularSwaggerView, SpectacularAPIView

from hashtag_app.api.views.hashtags import HashtagsView
from media_app.api.views.media import MediaView
#from publication_app.views import create_post_page
from publication_app.api.views.publications import PostsView
from publication_app.views import PostListView, PostCreateView

from media_app.api.router import api_router as media_router
from publication_app.api.router import api_router as publication_router
from hashtag_app.api.router import api_router as hashtags_router
from like_app.api.router import api_router as likes_router
from comments_app.api.router import api_router as comments_router
from account_app.api.router import api_router as accounts_router
from follower_app.api.router import api_router as follower_router

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('account_app.urls')),
    path("create_post/", PostCreateView.as_view(success_url=''), name = "create_post"),
    path('', PostListView.as_view(), name = 'home'),

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('api/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger'),

    path('medias/', include(media_router.urls)),
    path('posts/', include(publication_router.urls)),
    path('hashtags/', include(hashtags_router.urls)),
    path('like/', include(likes_router.urls)),
    path('comments/', include(comments_router.urls)),
    path('accounts/', include(accounts_router.urls)),
    path('subscription/', include(follower_router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    #path('api/publication/post_tags/<str:label>', PostsView.as_view({'get': 'post_tags'}))
]
#path('api/posts/', PostsView.as_view({'get':'list', 'post':'create'}), name = 'api-posts'),

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
