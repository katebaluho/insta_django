from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularRedocView, SpectacularSwaggerView, SpectacularAPIView

from account_app.views import registration_page, auth_page, profile_edit_page, profile_page
from hashtag_app.api.views.hashtags import HashtagsView
from publication_app.api.views.publications import PostsView
from publication_app.views import main_page, create_post_page
from publication_app.views import PostListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_page, name = 'home'),
    path('', include('account_app.urls')),
    path("create_post/", create_post_page, name = "create_post"),
    path('posts/', PostListView.as_view()),

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('api/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger'),
    path('api/posts/', PostsView.as_view({'get':'list', 'post':'create'}), name = 'api-posts'),
    path('api/hashtags/', HashtagsView.as_view({'get':'list', }), name = 'api-hashtags'),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
