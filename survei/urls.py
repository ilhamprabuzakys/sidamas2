from django.urls import path, include
from rest_framework import routers

from . import api
from . import views


router = routers.DefaultRouter()
# percobaan
router.register("tipe_survei", api.TipeSurveiViewSet)
router.register("data_survei", api.DataSurveiViewSet)
router.register("data_responden_survei", api.DataRespondenSurveiViewSet)
router.register("data_pengisian_survei", api.DataPengisianSurveiViewSet)
router.register("intelijen/sumber", api.DataIntelijenSumberSurveiViewSet)
router.register("intelijen/data", api.DataIntelijenSurveiViewSet)
router.register("intelijen/responden", api.DataIntelijenRespondenSurveiViewSet)

urlpatterns = (
    # DRA
    path("api/v1/", include(router.urls)),

    # menampilkan hasil survei satuan
    path("hasil_survei/<int:pk>/", views.hasil_surveiView.as_view(), name="hasil_survei"),
    path("hasil_survei_ls/<int:pk>/", views.hasil_survei_lsView.as_view(), name="hasil_survei_ls"),
    path("hasil_survei_kk/<int:pk>/", views.hasil_survei_kkView.as_view(), name="hasil_survei_kk"),

    # menampilkan hasil survei secara triwulan
    path("hasil_triwulan/<path:bulan>/<path:tahun>/<path:satker>/", views.hasil_survei_triwulanView.as_view(), name="hasil_survei_triwulan"),
    path("hasil_triwulan_ls/<path:bulan>/<path:tahun>/<path:satker>/", views.hasil_survei_triwulan_lsView.as_view(), name="hasil_survei_triwulan_ls"),
    path("hasil_triwulan_kk/<path:bulan>/<path:tahun>/<path:satker>/", views.hasil_survei_triwulan_kkView.as_view(), name="hasil_survei_triwulan_kk"),

    # menampilkan chart
    path("chart_survei/<int:pk>/", views.chart_surveiView.as_view(), name="hasil_survei"),
    path("chart_survei_kk/<int:pk>/", views.chart_survei_kkView.as_view(), name="hasil_survei"),
    path("chart_triwulan/<path:bulan>/<path:tahun>/", views.triwulan_surveiView.as_view(), name="triwulan_survei"),

    # persiapan variable xlsl
    path('generate_spreadsheet_tu/', views.generate_spreadsheet_tu, name='generate_spreadsheet_tu'),
    path('generate_spreadsheet_ls/', views.generate_spreadsheet_ls, name='generate_spreadsheet_ls'),
    path('generate_spreadsheet_kk/', views.generate_spreadsheet_kk, name='generate_spreadsheet_kk'),

    # download xlsl
    path('download_tu/', views.spreedsheet_tu, name='download_tu'),
    path('download_ls/', views.spreedsheet_ls, name='download_ls'),
    path('download_kk/', views.spreedsheet_kk, name='download_kk'),

    # api
    path("api/v1/datasurvei/triwulan/", api.DataSurveiViewSet.as_view({'post': 'triwulan'}), name="datasurvei_triwulan"),
    path("api/v1/datapengisiansurvei/triwulan/", api.DataPengisianSurveiViewSet.as_view({'post': 'triwulan'}), name="data_pengisian_survei"),
)
