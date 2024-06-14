from django.urls import path, include
from rest_framework import routers

from . import api
from . import views

app_name = "users"

router = routers.DefaultRouter()
router.register("users", api.UserViewSet)
router.register("profile", api.ProfileViewSet)
router.register("satker", api.SatkerViewSet)
router.register("reg_provinces", api.reg_provincesViewSet)
router.register("reg_regencies", api.reg_regenciesViewSet)
router.register("reg_district", api.reg_districtViewSet)
router.register("reg_villages", api.reg_villagesViewSet)
router.register("kegiatan_akun", api.KegiatanAkunViewSet)
router.register("uraian_kegiatan", api.UraianKegiatanViewSet)

urlpatterns = [
    path("api/v1/", include(router.urls)),
    path("registrasi/", views.RegistrasiUserView.as_view(), name="registrasi"),
    path("profile/", views.MyProfile.as_view(), name="index"),
    path("verifikasi/", views.UserVerificationListView.as_view(), name="list_verified"),
]