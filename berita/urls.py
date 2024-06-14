from django.urls import include, path
from rest_framework import routers

from . import views
from . import api

app_name = "berita"

router = routers.DefaultRouter()
router.register("", api.BeritaViewSet, basename="berita")

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("", views.BeritaListView.as_view(), name="list"),
    path("create/", views.BeritaCreateView.as_view(), name="create"),
    path("<int:pk>/", views.BeritaDetailView.as_view(), name="detail"),
)
