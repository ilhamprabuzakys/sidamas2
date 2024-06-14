from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from users.forms import UpdateUserForm, UpdateProfileForm
from django.shortcuts import redirect, render
from . import models
from sidamas.mixins import GlobalPermissionMixin

class UsersBaseView(GlobalPermissionMixin, LoginRequiredMixin):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list_satker'] = models.Satker.objects.all()
        context['list_satker_bnnp'] = models.SatkerBNNP.objects.order_by('nama_satker')
        context['list_satker_bnnk'] = models.SatkerBNNK.objects.order_by('nama_satker')
        context['list_provinsi'] = models.reg_provinces.objects.order_by('nama_provinsi')
        return context

class RegistrasiUserView(UsersBaseView, TemplateView):
    template_name = "users/registrasi/registrasi.html"

class UserVerificationListView(UsersBaseView, View):
    template_name = "users/verified/list_users.html"

    def get(self, request):
        user = request.user
        role = user.profile.role
        satker_id = user.profile.satker_id

        list_profile_users = models.Profile.objects.order_by('-id')
        satker = models.Satker.objects.get(id=satker_id)

        if role == "psm":
            list_profile_users = list_profile_users.filter(role="psm")
        elif role == "dayatif":
            list_profile_users = list_profile_users.filter(role="dayatif")

        if satker.level == 0:
            satker_list = models.Satker.filter(provinsi_id=satker.provinsi_id)
        elif satker.level == 1:
            satker_list = models.Satker.filter(id=satker.id)
        elif satker.level == 2:
            satker_list = models.Satker.objects.all()

        context =   {
                        "list_profile_users": list_profile_users,
                        "daftar_satker":satker_list
                    }
        return render(request, self.template_name, context)

class MyProfile(LoginRequiredMixin,View):

    def get(self, request):
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

        context = {
            'user_form': user_form,
            'profile_form': profile_form
        }

        return render(request, 'profile.html', context)

    def post(self,request):
        user_form = UpdateUserForm(
            request.POST,
            instance=request.user
        )
        profile_form = UpdateProfileForm(
            request.POST,
            request.FILES,
            instance=request.user.profile
        )

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

            messages.success(request,'Your profile has been updated successfully')

            return redirect('dashboard:profile')
        else:
            context = {
                'user_form': user_form,
                'profile_form': profile_form
            }
            messages.error(request,'Error updating you profile')

            return render(request, 'users/profile.html', context)
