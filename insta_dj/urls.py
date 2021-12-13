from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from django.conf.urls.static import static

from account_app.views import registration_page, auth_page, profile_edit_page, profile_page
from publication_app.views import main_page, create_post_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_page, name = 'home'),
    path('', include('account_app.urls')),
    path("create_post/", create_post_page, name = "create_post")
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
