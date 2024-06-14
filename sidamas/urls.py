from django.contrib.sitemaps.views import sitemap
from django.views.generic import TemplateView
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .sitemaps import StaticViewSitemap, BeritaViewSitemap

sitemaps = {'static': StaticViewSitemap, 'berita': BeritaViewSitemap}

urlpatterns = [
    path("robots.txt",TemplateView.as_view(template_name="home/robots.txt", content_type="text/plain")),
    path("sitemap.xml", sitemap, {'sitemaps': sitemaps}, name="django.contrib.sitemaps.views.sitemap"),

    path("", include("home.urls")),
    path("accounts/", include("accounts.urls")),
    path("testmodule/", include("testmodule.urls")),
    path("admin/", admin.site.urls),
    path("kegiatan/", include("kegiatan.urls")),
    path("lk/", include("lk.urls")),
    path("survey/", include("survey.urls")),
    path("survei/", include("survei.urls")),
    path("dashboard/", include("dashboard.urls")),
    path("dashboard/berita/", include("berita.urls")),
    path("users/", include("users.urls")),
    path("dashboard/literasi/", include("literasi.urls")),
    # path("map/", include("map.urls")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns += static(settings.MEDIA_URL,
#                           document_root=settings.MEDIA_ROOT)

# Serve media files during development when DEBUG is True
# if settings.DEBUG:
