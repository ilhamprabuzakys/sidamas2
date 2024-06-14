import json
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, JsonResponse
from django.views.generic import TemplateView
from users.models import Profile, Satker
from django.urls import reverse

class GlobalPermissionMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser == False and request.user.is_staff == False and request.user.profile.role is None or request.user.profile.satker is None or request.user.profile.is_verified == False:
            user = self.request.user
            message = "Maaf " + user.username + ", anda tidak memiliki hak akses untuk mengunjungi halaman ini."
            print(message)
            return HttpResponseRedirect(reverse("dashboard:profile"))
        return super().dispatch(request, *args, **kwargs)

class DashboardBaseView(LoginRequiredMixin, GlobalPermissionMixin):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class DashboardView(DashboardBaseView, View):
    def get(self, request):
        if not self.request.user.profile.role or not self.request.user.profile.satker or not self.request.user.profile.is_verified:
            return HttpResponseRedirect(reverse("dashboard:profile"))

        context = {
            'satker': Satker.objects.exclude(level=2)
        }

        if self.request.user.profile.role == "psm":
            template_name = "dashboard/dashboard_index_psm.html"
        else:
            template_name = "dashboard/dashboard_index_dayatif.html"

        return render(request, template_name, context)

class DashboardViewOld(DashboardBaseView, View):
    def get(self, request):
        if not self.request.user.profile.role or not self.request.user.profile.satker or not self.request.user.profile.is_verified:
            return HttpResponseRedirect(reverse("dashboard:profile"))

        context = {
            'satker': Satker.objects.exclude(level=2)
        }

        if self.request.user.profile.role == "psm":
            template_name = "dashboard/dashboard_index_psm.html"
        else:
            template_name = "dashboard/dashboard_index_dayatif_old.html"

        return render(request, template_name, context)

class ProfilView(LoginRequiredMixin, View):
    template_name = "dashboard/pengaturan/profile.html"
    daftar_direktorat = [
        {
            'value': 'psm',
            'label': 'PSM',
        },
        {
            'value': 'dayatif',
            'label': 'Dayatif',
        }
    ]

    def get(self, request):
        user = self.request.user
        context = {
            "daftar_direktorat": self.daftar_direktorat,
            "daftar_satker": Satker.objects.all()
        }
        print(f'User role {user.profile.role}')
        print(f'User satker {user.profile.satker}')
        print(f'User is_verified {user.profile.is_verified}')
        print('Hasil keseluruhan: ', user.profile.role and user.profile.satker and user.profile.is_verified)

        return render(request, self.template_name, context)

    def post(self, request):
        try:
            if self.request.GET.get('update') == 'avatar':
                print('Memperbarui avatar...')
                avatar_file = request.FILES.get('avatar')
                if avatar_file:
                    request.user.profile.avatar = avatar_file
                    request.user.profile.save()
                    return JsonResponse({'success': True, 'detail': 'Berhasil memperbarui avatar', 'avatar': request.user.profile.avatar.url})
                else:
                    return JsonResponse({'success': False, 'error': 'No file uploaded'})
            else:
                print('Memperbarui profile information...')

                data = json.loads(request.body.decode('utf-8'))
                print('Data POST:', data)
                data_user = self.request.user

                print('Data user:', data_user)

                data_profile = get_object_or_404(Profile, user=data_user)

                data_user.first_name = data.get('first_name', '')
                data_user.last_name = data.get('last_name', '')
                # Save user email
                data_user.email = data.get('email', '')
                data_user.save()


                if data.get('satker', '') != '':
                    satker_instance = get_object_or_404(Satker, nama_satker=data.get('satker', ''))
                    data_profile.satker = satker_instance

                data_profile.role = data.get('direktorat', '')
                data_profile.save()

                print('Data user sudah diperbarui:', data_user.first_name)
                print('Data user profile direktorat sudah diperbarui:', data_profile.role)
                print('Data user profile satker sudah diperbarui:', data_profile.satker)

                return JsonResponse({'success': True, 'detail': 'Berhasil memperbarui profile'})
        except json.JSONDecodeError as e:
            print('Error decoding JSON:', str(e))
            return JsonResponse({'success': False, 'error': 'Invalid JSON format'})


class KeamananView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard/pengaturan/keamanan.html"