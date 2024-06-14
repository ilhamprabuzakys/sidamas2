from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import View
from django.views.generic import TemplateView
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import render
from kegiatan import models
from django.db.models import Q
from users.models import Satker, Observasi, Kegiatan_akun

from sidamas.mixins import (GlobalPermissionMixin, PsmPermissionMixin, DayatifPermissionMixin, BNNPPermissionMixin)

class PSMBaseView(LoginRequiredMixin, GlobalPermissionMixin, PsmPermissionMixin):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class psm_rakernisView(PSMBaseView, View):
    template_name = "psm/rakernis/rakernis.html"

    def get(self, request):
        satker = Satker.objects.all()
        return render(request, self.template_name, {'satker' : satker})

class psm_rakernis2View(PSMBaseView, View):
    template_name = "psm/rakernis/rakernis2.html"

    def get(self, request):
        satker = Satker.objects.all()
        return render(request, self.template_name, {'satker' : satker})

class psm_rakernis3View(PSMBaseView, View):
    template_name = "psm/rakernis/rakernis3.html"

    def get(self, request):
        satker = Satker.objects.all()
        return render(request, self.template_name, {'satker' : satker})

class psm_bintekView(PSMBaseView, BNNPPermissionMixin, View):
    template_name = "psm/bintek/bintek.html"

    def get(self, request):
        user_satker = self.request.user.profile.satker
        satker = Satker.objects.all()
        context = {
             'satker': satker
        }
        if user_satker.level == 0:
            context['satker_target'] = Satker.objects.filter(parent=user_satker.pk)
        else:
            context['satker_target'] = Satker.objects.all()

        return render(request, self.template_name, context)

class psm_rakor_pemetaanView(PSMBaseView, View):
    template_name = "psm/rakor_pemetaan/rakor_pemetaan.html"

    def get(self, request):
        satker = Satker.objects.all()
        return render(request, self.template_name, {'satker' : satker})

class psm_rakor_pemetaanView_2(PSMBaseView, View):
    template_name = "psm/rakor_pemetaan2/index.html"

    def get(self, request):
        satker = Satker.objects.all()
        return render(request, self.template_name, {'satker' : satker})

class psm_audiensiView(PSMBaseView, View):
    template_name = "psm/audiensi/audiensi.html"

    def get(self, request):
        satker = Satker.objects.all()
        return render(request, self.template_name, {'satker' : satker})

class psm_konsolidasi_kebijakanView(PSMBaseView, View):
    template_name = "psm/konsolidasi_kebijakan/konsolidasi_kebijakan.html"

    def get(self, request):
        satker = Satker.objects.all()
        return render(request, self.template_name, {'satker' : satker})

class psm_workshop_penggiatView(PSMBaseView, View):
    template_name = "psm/workshop_penggiat/workshop_penggiat.html"

    def get(self, request):
        satker = Satker.objects.all()
        return render(request, self.template_name, {'satker' : satker})

class psm_bimtek_penggiat_p4gnView(PSMBaseView, View):
    template_name = "psm/bimtek_penggiat_p4gn/bimtek_penggiat_p4gn.html"

    def get(self, request):
        satker = Satker.objects.all()
        return render(request, self.template_name, {'satker' : satker})


class psm_sinkronisasi_kebijakanView(PSMBaseView, View):
    template_name = "psm/sinkronisasi_kebijakan/sinkronisasi_kebijakan.html"

    def get(self, request):
            satker = Satker.objects.all()
            return render(request, self.template_name, {'satker' : satker})

class psm_workshop_tematikView(PSMBaseView, View):
    template_name = "psm/workshop_tematik/workshop_tematik.html"

    def get(self, request):
            satker = Satker.objects.all()
            return render(request, self.template_name, {'satker' : satker})

class psm_asistensiView(PSMBaseView, View):
    template_name = "psm/asistensi/asistensi.html"

    def get(self, request):
            satker = Satker.objects.all()
            return render(request, self.template_name, {'satker' : satker})

class psm_tes_urine_deteksi_diniView(PSMBaseView, View):
    template_name = "psm/tes_urine_deteksi_dini/tes_urine_deteksi_dini.html"

    def get(self, request):
            satker = Satker.objects.all()
            return render(request, self.template_name, {'satker' : satker})

class psm_monev_supervisi_kegiatan_kotanView(PSMBaseView, View):
    template_name = "psm/monev_supervisi_kegiatan_kotan/monev_supervisi_kegiatan_kotan.html"

    def get(self, request):
            satker = Satker.objects.all()
            return render(request, self.template_name, {'satker' : satker})

class psm_pengumpulan_data_ikotanView(PSMBaseView, View):
    template_name = "psm/pengumpulan_data_ikotan/pengumpulan_data_ikotan.html"

    def get(self, request):
            satker = Satker.objects.all()
            observasi = Observasi.objects.all()
            return render(request, self.template_name, {'satker' : satker, 'observasi' : observasi})

class psm_dukungan_stakeholderView(PSMBaseView, View):
    template_name = "psm/dukungan_stakeholder/dukungan_stakeholder.html"

    def get(self, request):
            satker = Satker.objects.all()
            return render(request, self.template_name, {'satker' : satker})

class psm_kegiatan_lainnyaView(PSMBaseView, View):
    template_name = "psm/kegiatan_lainnya/kegiatan_lainnya.html"

    def get(self, request):
            satker = Satker.objects.all()
            kegiatan_akun = Kegiatan_akun.objects.all()
            return render(request, self.template_name, {'satker' : satker, 'kegiatan_akun' : kegiatan_akun})

class psm_jadwal_kegiatan_tahunanView(PSMBaseView, View):
    template_name = "psm/jadwal_kegiatan_tahunan/jadwal_kegiatan_tahunan.html"

    def get(self, request):
            satker = Satker.objects.all()
            kegiatan_akun = Kegiatan_akun.objects.all()
            return render(request, self.template_name, {'satker' : satker, 'kegiatan_akun' : kegiatan_akun})