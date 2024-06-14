import json
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, resolve_url
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView

class CustomLoginView(LoginView):
    # MIX using a vue component
    template_name = "auth/login_vue.html"
    redirect_authenticated_user = True

    def form_invalid(self, form):
        response = super().form_invalid(form)
        messages.error(self.request, 'Masukan yang Anda berikan tidak valid. Harap periksa kembali.')
        return response
    
    def get_success_url(self):
        data_user = self.request.user
        data_user_profile = data_user.profile
        
        print(f'User {data_user} berhasil login ...')
        
        if data_user_profile is None:
            logout()
            return HttpResponseForbidden("Terjadi kesalahan, tolong login ulang.")
        
        print('Data user profile :', data_user_profile)
        
        satker_value = getattr(data_user_profile, 'satker', None)
        role_value = getattr(data_user_profile, 'role', None)
        
        print('Data user satker: ', satker_value)
        print('Data user direktorat: ', role_value)
        
        next_url = self.request.GET.get('next', None)
        
        if satker_value is None:
            return reverse("dashboard:profile")
        elif role_value is None:
            return reverse("pilih_direktorat")
        elif satker_value and role_value:
            if next_url:
                return next_url
            else:
                return reverse("dashboard:index")
    
class HandleLoginLogic(LoginRequiredMixin, View):
    def get(self, request):
        user = self.request.user
        
        print(f'Data user: {user}')
        
        if user.profile is None:
            logout()
            return HttpResponseForbidden("Terjadi kesalahan, tolong login ulang.")
        
        print('Data user profile: ', user.profile)
        
        satker_value = getattr(user.profile, 'satker', None)
        role_value = getattr(user.profile, 'role', None)
        
        print(f'Data user satker: {satker_value}')
        print(f'Data user direktorat: {role_value}')
        
        next_url = self.request.GET.get('next', None)
    
        if satker_value is None:
            return HttpResponseRedirect(reverse("dashboard:profile"))
        elif role_value is None:
            return HttpResponseRedirect(reverse("pilih_direktorat"))
        elif satker_value and role_value:
            if next_url:
                return HttpResponseRedirect(next_url)
            else:
                return HttpResponseRedirect(reverse("dashboard:index"))


class PilihDirektoratView(LoginRequiredMixin, View):
    template_name = "auth/pilih_direktorat.html"
    
    def get(self, request):
        user = self.request.user # return -> object user
        user_direktorat = user.profile.role # return -> psm, dayatif
        
        is_staff = user.is_staff
        is_superuser = user.is_superuser
        
        print(f'is_superuser: {is_superuser}')
        print(f'is_staff: {is_staff}')
        
        if is_superuser or is_staff:
            return HttpResponseRedirect(reverse("dashboard:index"))
        elif user_direktorat in [None, '']:
            return render(request, self.template_name)
        else:
            return HttpResponseRedirect(reverse("dashboard:index"))

class CustomLogoutView(LogoutView):
    template_name = "auth/login.html"
    next_page = "selesai_logout"

# class LupaPasswordView(TemplateView):
#     template_name = "auth/lupa_password.html"

# class ResetPasswordView(TemplateView):
#     template_name = "auth/reset_password.html"
    
class LoggedOutView(TemplateView):
    template_name = "auth/logged_out.html"
    
