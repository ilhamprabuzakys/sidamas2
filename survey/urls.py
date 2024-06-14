from django.urls import path, include
from rest_framework import routers

from . import api
from . import views


router = routers.DefaultRouter()
router.register("survey", api.surveyViewSet)
router.register("survey_create", api.surveycreateViewSet)
router.register("surveyshort", api.surveyshortViewSet)
router.register("survey_result", api.survey_resultViewSet)


urlpatterns = (
    path("api/v1/", include(router.urls)),
    # Punya Bapak
    path("eform/", views.eFormView.as_view(), name="eform"),
    path("eform/create/", views.eFormCreateView.as_view(), name="eform_create"),
    path("eform/edit/<int:id>/", views.eFormEditView.as_view(), name="eform_edit"),
    path("eform/shortcode/", views.eFormShortView.as_view(), name="eform_shortcode"),
    path("go/<str:id>/", views.eFormGoSurveyView.as_view(), name="eform_view_shortcode"),
    path("create_short/<int:id>/", views.create_sc, name="create_shortcode"),
    path("pwa/", views.PWAView.as_view(), name="pwa"),
    # Custom
    path("formulir_elektronik/", views.FormulirElektronikView.as_view(), name="formulir_elektronik"),
    path("formulir_elektronik/create/", views.FormulirElektronikCreateView.as_view(), name="formulir_elektronik_create"),
    path("formulir_elektronik/edit/<int:id>/", views.FormulirElektronikEditView.as_view(), name="formulir_elektronik_edit"),
    path("formulir_elektronik/result/<int:id>/", views.FormulirElektronikResultView.as_view(), name="formulir_elektronik_result"),
    path("formulir_elektronik/view/<slug:slug>/", views.FormulirElektronikViewView.as_view(), name="formulir_elektronik_view"),
    # PSM
    path("psm/skm_tes_urine/", views.SKMTesUrineView.as_view(), name="psm_skm_tes_urine"),
    # Dayatif
    path("dayatif/skm_life_skill/", views.SKMLifeSkill.as_view(), name="dayatif_skm_life_skill"),
    path("dayatif/keberhasilan_kewirausahaan/", views.KeberhasilanKewirausahaanView.as_view(), name="dayatif_keberhasilan_kewirausahaan"),
    path("dayatif/survei_ikrn/", views.SurveiIKRNView.as_view(), name="dayatif_survei_ikrn"),
    path("dayatif/survei_ikrn/create/", views.SurveiIKRNCreateView.as_view(), name="dayatif_survei_ikrn_create"),
    path("dayatif/survei_ikrn/<int:id>/", views.SurveiIKRNDetailView.as_view(), name="dayatif_survei_ikrn_detail"),
    path("dayatif/survei_ikrn/<int:id>/edit/", views.SurveiIKRNEditView.as_view(), name="dayatif_survei_ikrn_edit"),
)
