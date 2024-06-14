from django.urls import path, include
from rest_framework import routers

from . import api
from . import views

router = routers.DefaultRouter()
router.register("user", api.userViewSet)
router.register("image", api.ImageModelViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("testmodule/user/", views.userListView.as_view(), name="testmodule_user_list"),
    path("testmodule/user/create/", views.userCreateView.as_view(), name="testmodule_user_create"),
    path("testmodule/user/detail/<int:pk>/", views.userDetailView.as_view(), name="testmodule_user_detail"),
    path("testmodule/user/update/<int:pk>/", views.userUpdateView.as_view(), name="testmodule_user_update"),
    path("testmodule/user/delete/<int:pk>/", views.userDeleteView.as_view(), name="testmodule_user_delete"),
    # url tambahan
    path("test/", views.testdatatables),
    path("testchart/", views.testchart),
    path("testeform/", views.testeform),
    path("testsurvey/", views.testsurvey),
    path("testinteraktif/", views.testinteraktif),
    path('export/', views.ExportDataView.as_view(), name='export_data'),
    path('export_img/', views.ExportDataImg.as_view(), name='export_data_img'),
)
