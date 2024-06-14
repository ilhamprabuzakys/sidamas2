from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.views import View, generic
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from . import models

class GlobalPermissionMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser == False and request.user.is_staff == False and request.user.profile.role is None or request.user.profile.satker is None or request.user.profile.is_verified == False:
            user = self.request.user
            message = "Maaf " + user.username + ", anda tidak memiliki hak akses untuk mengunjungi halaman ini."
            print(message)
            return HttpResponseRedirect(reverse("dashboard:profile"))
        return super().dispatch(request, *args, **kwargs)
    
class LiterasiBaseView(GlobalPermissionMixin, LoginRequiredMixin):
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class LiterasiView(LiterasiBaseView, View):
    template_name = "literasi/list_literasi.html"
    def get(self, request):
        context = {
            "list_literasi" : models.Literasi.objects.all(),
            "list_status" : models.Literasi.STATUS_CHOICES
        }
        
        return render(request, self.template_name, context)