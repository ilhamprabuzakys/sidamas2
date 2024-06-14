from django.urls import path
from . import views

app_name = "berita"

urlpatterns = (
    path("", views.BeritaListView.as_view(), name="list"),
    path("create/", views.BeritaCreateView.as_view(), name="create"),
    path("<int:pk>/", views.BeritaDetailView.as_view(), name="detail"),
)
