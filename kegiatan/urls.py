from django.urls import path, include
from rest_framework import routers
from . import api
from . import views

router = routers.DefaultRouter()

# ==== PSM ====
psm = routers.DefaultRouter()
psm.register("rakernis", api.PSM_RAKERNIS_ViewSet)
psm.register("binaan_teknis", api.PSM_BINAAN_TEKNIS_ViewSet)
psm.register("asistensi", api.PSM_ASISTENSI_ViewSet)
psm.register("tes_urine", api.PSM_TES_URINE_DETEKSI_DINI_ViewSet)
psm.register("tes_urine_crud", api.PSM_TES_URNIE_CURD_ViewSet) #crud;
psm.register("monev_supervisi", api.PSM_MONITORING_DAN_EVALUASI_SUPERVISI_ViewSet)
psm.register("monev_supervisi_crud", api.PSM_MONITORING_DAN_EVALUASI_SUPERVISI_CURD_ViewSet) #crud;
psm.register("pengumpulan_data_ikotan", api.PSM_PENGUMPULAN_DATA_IKOTAN_ViewSet)
psm.register("pengumpulan_data_ikotan_crud", api.PSM_PENGUMPULAN_DATA_IKOTAN_CURD_ViewSet) #crud;
psm.register("dukungan_stakeholder", api.PSM_DUKUNGAN_STAKEHOLDER_ViewSet)
psm.register("dukungan_stakeholder_crud", api.PSM_DUKUNGAN_STAKEHOLDER_CURD_ViewSet) #crud;
psm.register("kegiatan_lainnya", api.PSM_KEGIATAN_LAINNYA_ViewSet)
psm.register("kegiatan_lainnya_crud", api.PSM_KEGIATAN_LAINNYA_CURD_ViewSet) #crud;
psm.register("rakor_pemetaan", api.PSM_RAKOR_PEMETAAN_ViewSet)
psm.register("audiensi", api.PSM_AUDIENSI_ViewSet)
psm.register("konsolidasi_kebijakan", api.PSM_KONSOLIDASI_KEBIJAKAN_ViewSet)
psm.register("workshop_penggiat", api.PSM_WORKSHOP_PENGGIAT_ViewSet)
psm.register("workshop_tematik", api.PSM_WORKSHOP_TEMATIK_ViewSet)
psm.register("sinkronisasi_kebijakan", api.PSM_SINKRONISASI_KEBIJAKAN_ViewSet)
psm.register("bimtek_penggiat_p4gn", api.PSM_BIMTEK_P4GN_ViewSet)
psm.register("bimtek_penggiat_p4gn_count", api.PSM_BINTEK_P4GN_ViewSet)
psm.register("jadwal_kegiatan_tahunan", api.PSM_JADWAL_KEGIATAN_TAHUNAN_ViewSet)
psm.register("jadwal_kegiatan_tahunan_crud", api.PSM_JADWAL_KEGIATAN_TAHUNAN_CURD_ViewSet) #crud;
psm.register("jadwal", api.PSM_JADWAL_ViewSet) #crud;

# ==== DAYATIF (8 Modules) ====
dayatif = routers.DefaultRouter()
dayatif.register("satker", api.DAYATIF_KEGIATAN_SATKER_ViewSet, basename='satker')
dayatif.register("binaan_teknis", api.DAYATIF_BINAAN_TEKNIS_ViewSet, basename='binaan_teknis')
dayatif.register("pemetaan_potensi", api.DAYATIF_PEMETAAN_POTENSI_ViewSet, basename='pemetaan_potensi')
dayatif.register("pemetaan_stakeholder", api.DAYATIF_PEMETAAN_STAKEHOLDER_ViewSet, basename='pemetaan_stakeholder')
dayatif.register("rapat_sinergi_stakeholder", api.DAYATIF_RAPAT_SINERGI_STAKEHOLDER_ViewSet, basename='rapat_sinergi_stakehotalder')
dayatif.register("bimbingan_teknis_stakeholder", api.DAYATIF_BIMBINGAN_TEKNIS_STAKEHOLDER_ViewSet, basename='bimbingan_teknis_stakeholder')
dayatif.register("bimbingan_teknis_lifeskill", api.DAYATIF_BIMBINGAN_TEKNIS_LIFESKILL_ViewSet, basename='bimbingan_teknis_lifeskill')
dayatif.register("monev_dayatif", api.DAYATIF_MONEV_DAYATIF_ViewSet, basename='monev_dayatif')
dayatif.register("dukungan_stakeholder", api.DAYATIF_DUKUNGAN_STAKEHOLDER_ViewSet, basename='dukungan_stakeholder')

router.registry.extend(psm.registry)
router.registry.extend(dayatif.registry)

urlpatterns = (
    path("api/v1/psm/", include(psm.urls), name='psm-list'),
    path("api/v1/dayatif/", include(dayatif.urls), name='dayatif-list'),

    # API Root
    path("api/v1/", api.api_root, name="Daftar Direktorat"),

    path("api/v1/dayatif/satker_kegiatan/", api.DAYATIF_SatkerCountView.as_view(), name="dayatif_satker_kegiatan"),
    path("api/v1/dayatif/kegiatan_count/", api.DAYATIF_KegiatanCountView.as_view(), name="dayatif_kegiatan"),
    path("api/v1/dayatif/survei_count/", api.DAYATIF_SurveiCountView.as_view(), name="dayatif_survei"),
    # psm
    path("api/v1/psm/kegiatan_count/", api.PSM_KegiatanCountView.as_view(), name="psm_kegiatan"),
    path("api/v1/psm/survei_count/", api.PSM_SurveiCountView.as_view(), name="psm_survei"),

    # VIEW HALAMAN PSM
    path("psm/rakernis/",views.psm_rakernisView.as_view(),name="psm_rakernis",),
    path("psm/rakernis2/",views.psm_rakernis2View.as_view(),name="psm_rakernis2",),
    path("psm/rakernis3/",views.psm_rakernis3View.as_view(),name="psm_rakernis2",),
    path("psm/bintek/",views.psm_bintekView.as_view(),name="psm_bintek",),
    path("psm/rakor_pemetaan/",views.psm_rakor_pemetaanView.as_view(),name="psm_rakor_pemetaan",),
    path("psm/rakor_pemetaan2/",views.psm_rakor_pemetaanView_2.as_view(),name="psm_rakor_pemetaan2",),
    path("psm/audiensi/",views.psm_audiensiView.as_view(),name="psm_audiensi",),
    path("psm/konsolidasi_kebijakan/",views.psm_konsolidasi_kebijakanView.as_view(),name="psm_konsolidasi_kebijakan",),
    path("psm/workshop_penggiat/",views.psm_workshop_penggiatView.as_view(),name="psm_workshop_penggiat",),
    path("psm/bimtek_peggiat_p4gn/",views.psm_bimtek_penggiat_p4gnView.as_view(),name="psm_bimtek_penggiat_p4gn",),
    path("psm/sinkronisasi_kebijakan/",views.psm_sinkronisasi_kebijakanView.as_view(),name="psm_sinkronisasi_kebijakan",),
    path("psm/workshop_tematik/",views.psm_workshop_tematikView.as_view(),name="psm_workshop_tematik",),
    path("psm/asistensi/",views.psm_asistensiView.as_view(),name="psm_asistensi",),
    path("psm/tes_urine/",views.psm_tes_urine_deteksi_diniView.as_view(),name="psm_tes_urine",),
    path("psm/monev_supervisi_kegiatan_kotan/",views.psm_monev_supervisi_kegiatan_kotanView.as_view(),name="psm_monev_supervisi_kegiatan_kotan",),
    path("psm/pengumpulan_data_ikotan/",views.psm_pengumpulan_data_ikotanView.as_view(),name="psm_pengumpulan_data_ikotan",),
    path("psm/dukungan_stakeholder/",views.psm_dukungan_stakeholderView.as_view(),name="psm_dukungan_stakeholder",),
    path("psm/kegiatan_lainnya/",views.psm_kegiatan_lainnyaView.as_view(),name="psm_kegiatan_lainnya",),
    path("psm/jadwal_kegiatan_tahunan/",views.psm_jadwal_kegiatan_tahunanView.as_view(),name="psm_jadwal_kegiatan_tahunan",),

    # VIEW HALAMAN DAYATIF
    path("dayatif/binaan_teknis/",views.DAYATIF_BINAAN_TEKNIS_View.as_view(),name="dayatif_binaan_teknis",),
    path("dayatif/pemetaan_potensi/",views.DAYATIF_PEMETAAN_POTENSI_View.as_view(),name="dayatif_pemetaan_potensi",),
    path("dayatif/pemetaan_stakeholder/",views.DAYATIF_PEMETAAN_STAKEHOLDER_View.as_view(),name="dayatif_pemetaan_stakeholder",),
    path("dayatif/rapat_sinergi_stakeholder/",views.DAYATIF_RAPAT_SINERGI_STAKEHOLDER_View.as_view(),name="dayatif_rapat_sinergi_stakeholder",),
    path("dayatif/bimbingan_teknis_stakeholder/",views.DAYATIF_BIMBINGAN_TEKNIS_STAKEHOLDER_View.as_view(),name="dayatif_bimbingan_teknis_stakeholder",),
    path("dayatif/bimbingan_teknis_lifeskill/",views.DAYATIF_BIMBINGAN_TEKNIS_LIFESKILL_View.as_view(),name="dayatif_bimbingan_teknis_lifeskill",),
    path("dayatif/monev_dayatif/",views.DAYATIF_MONEV_DAYATiF_View.as_view(),name="dayatif_monev_dayatif",),
    path("dayatif/dukungan_stakeholder/",views.DAYATIF_DUKUNGAN_STAKEHOLDER_View.as_view(),name="dayatif_dukungan_stakeholder",),
)