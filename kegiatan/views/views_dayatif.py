from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import View
from django.views.generic import TemplateView
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import render
from kegiatan import models
from django.db.models import Q
from users.models import Satker

from sidamas.mixins import (GlobalPermissionMixin, PsmPermissionMixin, DayatifPermissionMixin, BNNPPermissionMixin)

class DayatifBaseView(LoginRequiredMixin, GlobalPermissionMixin, DayatifPermissionMixin):
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['satker'] = Satker.objects.all()
        return context
    
# ======= BINAAN TEKNIS =======
class DAYATIF_BINAAN_TEKNIS_View(DayatifBaseView, BNNPPermissionMixin, TemplateView):
    template_name = "dayatif/binaan_teknis/binaan_teknis.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        satker = self.request.user.profile.satker
        
        if satker.level == 0:
            context['satker_target'] = Satker.objects.filter(parent=satker.pk)
        else:
            context['satker_target'] = Satker.objects.all()
        return context

# ======= PEMETAAN POTENSI =======
class DAYATIF_PEMETAAN_POTENSI_View(DayatifBaseView, TemplateView):
    template_name = "dayatif/pemetaan_potensi/pemetaan_potensi.html"

# ======= PEMETAAN STAKEHOLDER =======
class DAYATIF_PEMETAAN_STAKEHOLDER_View(DayatifBaseView, TemplateView):
    template_name = "dayatif/pemetaan_stakeholder/pemetaan_stakeholder.html"

# ======= RAPAT SINERGI STAKEHOLDER =======
class DAYATIF_RAPAT_SINERGI_STAKEHOLDER_View(DayatifBaseView, TemplateView):
    template_name = "dayatif/rapat_sinergi_stakeholder/rapat_sinergi_stakeholder.html"
    
# ======= BIMBINGAN_TEKNIS_STAKEHOLDER =======
class DAYATIF_BIMBINGAN_TEKNIS_STAKEHOLDER_View(DayatifBaseView, TemplateView):
    template_name = "dayatif/bimbingan_teknis_stakeholder/bimbingan_teknis_stakeholder.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        daftar_jenis_bimbingan = [
            {
                'value': 'bimbingan_teknis_stakeholder',
                'label': 'Bimbingan Teknis Stakeholder',
            },
            {
                'value': 'bimbingan_teknis_pendamping',
                'label': 'Bimbingan Teknis Pendamping',
            }
        ]
        context['daftar_jenis_bimbingan'] = daftar_jenis_bimbingan
        
        return context

# ======= BIMBINGAN_TEKNIS_LIFESKILL =======
class DAYATIF_BIMBINGAN_TEKNIS_LIFESKILL_View(DayatifBaseView, TemplateView):
    template_name = "dayatif/bimbingan_teknis_lifeskill/bimbingan_teknis_lifeskill.html"

# ======= MONEV_DAYATiF =======
class DAYATIF_MONEV_DAYATiF_View(DayatifBaseView, TemplateView):
    template_name = "dayatif/monev_dayatif/monev_dayatif.html"

# ======= DUKUNGAN_STAKEHOLDER =======
class DAYATIF_DUKUNGAN_STAKEHOLDER_View(DayatifBaseView, TemplateView):
    template_name = "dayatif/dukungan_stakeholder/dukungan_stakeholder.html"
