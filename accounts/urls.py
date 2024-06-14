from django.urls import path, include
from rest_framework import routers

from . import api
from . import views

# router = routers.DefaultRouter()
# router.register("pilih-direktorat", api.PilihDirektoratViewSet, basename='pilih-direktorat')

urlpatterns = (
    # path("api/v1/", include(router.urls)),
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('selesai-logout/', views.LoggedOutView.as_view(), name='selesai_logout'),
    
    # path("pilih-direktorat/", views.PilihDirektoratView.as_view(), name="pilih_direktorat"),
    # path("lupa-password/", views.LupaPasswordView.as_view(), name="lupa_password"),
    # path("reset-password/", views.ResetPasswordView.as_view(), name="reset_password"),
    
    # 👇 Handle login logic (also already handle how next page behavior)
    path("check-login/", views.HandleLoginLogic.as_view(), name="handle_login"),
)
