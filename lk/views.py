from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import render
from django.views import View, generic
from django.urls import reverse, reverse_lazy
from . import models
from . import forms

class GlobalPermissionMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser == False and request.user.is_staff == False and request.user.profile.role is None or request.user.profile.satker is None or request.user.profile.is_verified == False:
            user = self.request.user
            message = "Maaf " + user.username + ", anda tidak memiliki hak akses untuk mengunjungi halaman ini."
            print(message)
            return HttpResponseRedirect(reverse("dashboard:profile"))
        return super().dispatch(request, *args, **kwargs)
    
    
class LaporanKegiatanBaseView(GlobalPermissionMixin, LoginRequiredMixin):
    template_name = "laporan_kegiatan/list_lk.html"
    
    daftar_satuan = [
        {
            'value': 'Data',
            'label': 'Data',
        },
        {
            'value': 'Surat',
            'label': 'Surat',
        },
        {
            'value': 'Berkas',
            'label': 'Berkas',
        },
        {
            'value': 'Laporan',
            'label': 'Laporan',
        },
        {
            'value': 'Program',
            'label': 'Program',
        },
        {
            'value': 'Dokumen',
            'label': 'Dokumen',
        },
        {
            'value': 'Naskah',
            'label': 'Naskah',
        },
        {
            'value': 'Kegiatan',
            'label': 'Kegiatan',
        },
        {
            'value': 'Bahan',
            'label': 'Bahan',
        },
        {
            'value': 'Daftar',
            'label': 'Daftar',
        },
        {
            'value': 'Konsep Surat',
            'label': 'Konsep Surat',
        },
        {
            'value': 'Berita Acara',
            'label': 'Berita Acara',
        },
    ]
    
    def get(self, request):
        direktorat = self.request.user.profile.role
        is_superuser = request.user.is_superuser
        
        if not is_superuser and direktorat != self.allowed_direktorat:
            return HttpResponseForbidden("Anda tidak memiliki hak akses untuk mengunjungi halaman ini.")
            
        context = { "nama_direktorat" : self.direktorat_name, "daftar_satuan" : self.daftar_satuan }
        return render(request, self.template_name, context=context)

class LaporanKegiatanPSMView(LaporanKegiatanBaseView, View):
    allowed_direktorat = 'psm'
    direktorat_name = 'PSM'

class LaporanKegiatanDayatifView(LaporanKegiatanBaseView, View):
    allowed_direktorat = 'dayatif'
    direktorat_name = 'Dayatif'

class LaporanKegiatanAdminDayatifView(LaporanKegiatanBaseView, View):
    allowed_direktorat = 'dayatif'
    direktorat_name = 'Dayatif'
    template_name = 'laporan_kegiatan/admin/list_lk.html'
    
    def get(self, request):
        return render(request, self.template_name)
    
class tbl_eformListView(generic.ListView):
    model = models.tbl_eform
    form_class = forms.tbl_eformForm


class tbl_eformCreateView(generic.CreateView):
    model = models.tbl_eform
    form_class = forms.tbl_eformForm


class tbl_eformDetailView(generic.DetailView):
    model = models.tbl_eform
    form_class = forms.tbl_eformForm


class tbl_eformUpdateView(generic.UpdateView):
    model = models.tbl_eform
    form_class = forms.tbl_eformForm
    pk_url_kwarg = "pk"


class tbl_eformDeleteView(generic.DeleteView):
    model = models.tbl_eform
    success_url = reverse_lazy("lk_tbl_eform_list")


class tbl_responden_eformListView(generic.ListView):
    model = models.tbl_responden_eform
    form_class = forms.tbl_responden_eformForm


class tbl_responden_eformCreateView(generic.CreateView):
    model = models.tbl_responden_eform
    form_class = forms.tbl_responden_eformForm


class tbl_responden_eformDetailView(generic.DetailView):
    model = models.tbl_responden_eform
    form_class = forms.tbl_responden_eformForm


class tbl_responden_eformUpdateView(generic.UpdateView):
    model = models.tbl_responden_eform
    form_class = forms.tbl_responden_eformForm
    pk_url_kwarg = "pk"


class tbl_responden_eformDeleteView(generic.DeleteView):
    model = models.tbl_responden_eform
    success_url = reverse_lazy("lk_tbl_responden_eform_list")