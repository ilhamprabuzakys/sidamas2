from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = "home"

urlpatterns = [
    path("", views.BerandaView.as_view(), name="index"),
    path("pengisian-survei/", views.SurveiView.as_view(), name="survei"),
    path("persiapan-survei-kewirausahaan/", views.SurveiPersiapanKewirausahaan.as_view(), name="survei_persiapan_kewirausahaan"),
    path("pengisian-survei-kewirausahaan/<int:responden>/<slug:slug>/", views.SurveiKewirausahaanView.as_view(), name="survei_kewirausahaan"),
    path("media-sosial/", views.MediaSosialView.as_view(), name="media_sosial"),
    path("literasi/", views.literasi_view, name="literasi"),
    # path("literasi/", views.LiterasiView.as_view(), name="literasi"),
    path("beranda-kegiatan/", views.BerandaKegiatanView.as_view(),
         name="beranda_kegiatan"),
    # path("berita", views.BeritaView.as_view(), name="daftar_berita"),
    path("berita/<slug:slug>/", views.BeritaDetailView.as_view(), name="detail_berita"),

    # 👇 Redirecting user here
    path("login/", views.redirect_user_to_login, name="redirect_user_to_login"),
    path("testing/", views.testingView.as_view(), name="LoginViews"),
    path("unduh/survei-ikrn/", views.UnduhSurveiIKRNView.as_view(), name="unduh_survei_ikrn"),

]
