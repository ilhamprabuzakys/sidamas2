

from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from berita.models import Berita


class StaticViewSitemap(Sitemap):
    def items(self):
        return ['home:index', 'home:media_sosial', 'home:survei', 'home:literasi', 'home:beranda_kegiatan']
    
    def location(self, item):
        return reverse(item)
    
class BeritaViewSitemap(Sitemap):
    def items(self):
        return Berita.objects.all()