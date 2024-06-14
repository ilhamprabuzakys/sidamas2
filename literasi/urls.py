from django.urls import path, include
from rest_framework import routers

from . import api
from . import views


router = routers.DefaultRouter()
router.register("", api.LiterasiViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("", views.LiterasiView.as_view(), name="literasi"),
)
