import json
from django.http import HttpResponseForbidden, HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_http_methods
from django.utils.html import escape
from django.utils.safestring import mark_safe
from django.contrib.auth import login, logout
from django.contrib import messages
from django.views import View
from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_exempt, xframe_options_sameorigin
from django.views.generic import TemplateView

from .authbe import SidamasLDAPBackend
from berita.models import Berita
from survei.models import DataSurvei, DataPengisianSurvei

from literasi.models import Literasi

class BerandaView(View):
    template_name = "home/beranda.html"

    def get(self, request):
        data = Berita.objects.filter(status='published')

        context = { "data": data }
        return render(request, self.template_name, context)

class SurveiView(View):
    template_name = "home/pengisian_survei.html"

    def get(self, request):
        return render(request, self.template_name)

class SurveiPersiapanKewirausahaan(View):
    template_name = "home/pengisian_survei_persiapan_kewirausahaan.html"

    def get(self, request):
        return render(request, self.template_name)

class MediaSosialView(TemplateView):
    template_name = "home/media_sosial.html"

class LiterasiView(View):
    template_name = "home/literasi.html"

    def get(self, request):
        daftar_literasi = Literasi.objects.all()
        #print(daftar_literasi)
        return render(request, self.template_name, { 'daftar_literasi' : daftar_literasi })

@xframe_options_sameorigin
def literasi_view(request):
        template_name = "home/literasi.html"
        daftar_literasi = Literasi.objects.all()
        #print(daftar_literasi)
        return render(request, template_name, { 'daftar_literasi' : daftar_literasi })

class BerandaKegiatanView(TemplateView):
    template_name = "home/beranda_kegiatan.html"

    # def get(self, request):
    #     return render(request, self.template_name)

class BeritaView(View):
    template_name = "home/berita.html"

    def get(self, request):
        return render(request, self.template_name)

class BeritaDetailView(View):
    template_name = "home/detail_berita.html"

    def get(self, request, slug):
        semua_berita = Berita.objects.all()
        data = Berita.objects.get(slug=slug)
        user_pembuat = data.created_by

        tags_list = [tag for tag in data.tags.split(',')]

        current_index = semua_berita.filter(slug=slug).first().pk
        total_berita = semua_berita.count()

        prev_index = current_index - 1 if current_index > 1 else None
        next_index = current_index + 1 if current_index < total_berita else None

        berita_sebelumnya = semua_berita.filter(pk=prev_index).first()
        berita_selanjutnya = semua_berita.filter(pk=next_index).first()

        context = {
            "id" : data.pk,
            "slug" : data.slug,
            "judul": data.judul,
            "kategori": data.kategori,
            "created_at": data.created_at,
            "updated_at": data.updated_at,
            "isi_berita": data.isi_berita,
            "status": data.status,
            "tags": data.tags,
            "tags_list": tags_list,
            "gambar_utama": data.gambar_utama,
            "created_by": data.created_by,
            "updated_by": data.updated_by,
            "kategori_id": data.kategori,
            "semua_berita": semua_berita,
            "berita_sebelumnya": berita_sebelumnya,
            "berita_selanjutnya": berita_selanjutnya,
            "author": user_pembuat
        }

        return render(request, self.template_name, context=context)

class SurveiKewirausahaanView(View):
    template_name = "home/pengisian_survei_kewirausahaan.html"

    def get(self, request, slug, responden):

        data_survei = DataSurvei.objects.get(kode=slug)

        try:
            data_isi_survei = DataPengisianSurvei.objects.get(responden=responden)
            data_isi_survei_ada = True
        except DataPengisianSurvei.DoesNotExist:
            data_isi_survei_ada = False

        context = { "data_id": data_survei.id,
                    "data_responden": responden,
                    "data_isi_responden": data_isi_survei_ada }

        return render(request, self.template_name, context)

def truncate_and_escape(text, max_words):
    """
    Escape HTML and truncate text to a maximum number of words.
    This is a helper function like a Django bleach
    """
    words = text.split(' ')
    if len(words) > max_words:
        truncated_text = ' '.join(words[:max_words]) + '...'
    else:
        truncated_text = ' '.join(words)

    truncated_text = truncated_text.lstrip('<p>').rstrip('</p>')

    return mark_safe(escape(truncated_text))

# Redirecting user
def redirect_user_to_login(request):
    return redirect(reverse('login'))

@method_decorator(require_http_methods(["GET", "POST"]), name='dispatch')
class testingView(View):
    template_name = "auth2/login.html"
    redirect_authenticated_user = True

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        # Your post method logic here
        return render(request, self.template_name)  # Update this line based on your post logic

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

class UnduhSurveiIKRNView(TemplateView):
    template_name = 'home/unduh/unduh_survei_ikrn.html'