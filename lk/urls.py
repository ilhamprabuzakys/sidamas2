from django.urls import path, include
from rest_framework import routers

from . import api
from . import views


router = routers.DefaultRouter()
router.register("tbl_eform", api.tbl_eformViewSet)
router.register("tbl_responden_eform", api.tbl_responden_eformViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("psm/", views.LaporanKegiatanPSMView.as_view(), name="psm_laporan_kegiatan"),
    path("dayatif/", views.LaporanKegiatanDayatifView.as_view(), name="dayatif_laporan_kegiatan"),
    path("dayatif/admin/", views.LaporanKegiatanAdminDayatifView.as_view(), name="dayatif_laporan_kegiatan_admin"),
    path("lk/tbl_eform/", views.tbl_eformListView.as_view(), name="lk_tbl_eform_list"),
    path("lk/tbl_eform/create/", views.tbl_eformCreateView.as_view(), name="lk_tbl_eform_create"),
    path("lk/tbl_eform/detail/<int:pk>/", views.tbl_eformDetailView.as_view(), name="lk_tbl_eform_detail"),
    path("lk/tbl_eform/update/<int:pk>/", views.tbl_eformUpdateView.as_view(), name="lk_tbl_eform_update"),
    path("lk/tbl_eform/delete/<int:pk>/", views.tbl_eformDeleteView.as_view(), name="lk_tbl_eform_delete"),
    path("lk/tbl_responden_eform/", views.tbl_responden_eformListView.as_view(), name="lk_tbl_responden_eform_list"),
    path("lk/tbl_responden_eform/create/", views.tbl_responden_eformCreateView.as_view(), name="lk_tbl_responden_eform_create"),
    path("lk/tbl_responden_eform/detail/<int:pk>/", views.tbl_responden_eformDetailView.as_view(), name="lk_tbl_responden_eform_detail"),
    path("lk/tbl_responden_eform/update/<int:pk>/", views.tbl_responden_eformUpdateView.as_view(), name="lk_tbl_responden_eform_update"),
    path("lk/tbl_responden_eform/delete/<int:pk>/", views.tbl_responden_eformDeleteView.as_view(), name="lk_tbl_responden_eform_delete"),

)