from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.template.defaultfilters import length
from django.views import View, generic
from django.urls import reverse, reverse_lazy
from django.core.serializers import serialize

from django.contrib.auth.models import User

from survei.models import DataSurvei, TipeSurvei
from . import models
from . import forms
from users.models import Profile, Satker
import json
import random
import string
import json
from django.http import HttpResponse, HttpResponseRedirect

class GlobalPermissionMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser == False and request.user.is_staff == False and request.user.profile.role is None or request.user.profile.satker is None or request.user.profile.is_verified == False:
            user = self.request.user
            message = "Maaf " + user.username + ", anda tidak memiliki hak akses untuk mengunjungi halaman ini."
            print(message)
            return HttpResponseRedirect(reverse("dashboard:profile"))
        return super().dispatch(request, *args, **kwargs)

class SurveyBaseView(LoginRequiredMixin, GlobalPermissionMixin):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

# Punya Bapak
def create_unique_id():
    return ''.join(random.choices(string.ascii_uppercase+string.digits, k=8))

def create_shortcode():
    id = create_unique_id()
    unique = False
    while not unique:
        print(id)
        try:
            if not models.shortcode.objects.get(code=id):
                unique = True
            else:
                id = create_unique_id()
        except:
            id = create_unique_id()
            unique = True
    models.shortcode.objects.create(code=id)
    return id

def create_sc(request, id):
    survey = models.survey.objects.get(pk=id)
    pemilik = request.user
    profil = Profile.objects.get(user=pemilik)
    sc = create_shortcode()
    short = models.surveyshort(satker=profil.satker, shortcode=sc, dibuat_oleh=pemilik,status='1',survey=survey)
    short.save()
    return HttpResponse(json.dumps({'shortcode':sc}), content_type='application/json')

class PWAView(View):
    def get(self, request):
        return render(request, "pages/eform.html")

class eFormView(View):
    def get(self, request):
        context = {'bc': [{'text':'Home','url':'/dashboard/'},{'text':'E-Form','url':'/survey/eform/'}]}
        return render(request, "pages/eform.html", context)

class eFormShortView(View):
    def get(self, request):
        return render(request, "pages/eform_shortcode.html")

class eFormGoSurveyView(View):
    def get(self, request,id):
        try:
            sc = models.surveyshort.objects.get(shortcode=id)
            survey = models.survey.objects.get(pk=sc.survey.id)
            context = {"survey_source": survey.jsontext, "id":id}
        except:
            context = {"survey_source": json.dumps({"title":"Kode Survey Keliru","pages": [{"name": "page1"}]}), "id":id}
        return render(request, "pages/go_survey.html",context)

class eFormCreateView(View):
    def get(self, request):
        return render(request, "pages/eform_create.html")

class eFormEditView(View):
    def get(self, request, id):
        survey = models.survey.objects.get(pk=id)
        context = {"survey_source": survey.jsontext, "id":id}
        print(context)
        return render(request, "pages/eform_edit.html", context)

# Punya custom
class FormulirElektronikView(SurveyBaseView, View):
    template_name = "formulir_elektronik/formulir_elektronik_new.html"

    def get(self, request):
        user_id = request.user.id
        role = Profile.objects.values_list('role', flat=True).get(user_id=user_id)
        satker = Profile.objects.values_list('satker_id', flat=True).get(user_id=user_id)

        list_survey = models.survey.objects.order_by('-id')

        if role == "psm":
            list_survey_users = list_survey.filter(pemilik=1)
        elif role == "dayatif":
            list_survey_users = list_survey.filter(pemilik=2)

        # Menambahkan jumlah hasil survey ke setiap survey dalam list_survey_users
        for survey in list_survey_users:
            survey.respondents = models.survey_result.objects.filter(survey=survey).count()

        additional_context = {
            'user_id': user_id,
            'role': role,
            'satker': satker,
            'list_survey_users':list_survey_users
        }

        return render(request, self.template_name, context=additional_context)

class FormulirElektronikCreateView(SurveyBaseView, View):
    template_name = "formulir_elektronik/create.html"

    def get(self, request):
        user_id = request.user.id
        role = Profile.objects.values_list('role', flat=True).get(user_id=user_id)
        satker = Profile.objects.values_list('satker_id', flat=True).get(user_id=user_id)

        additional_context = {
            'user_id': user_id,
            'role': role,
            'satker': satker,
        }

        return render(request, self.template_name, context=additional_context)

class FormulirElektronikEditView(SurveyBaseView, View):
    template_name = "formulir_elektronik/edit.html"

    def get(self, request, id):

        survey = models.survey.objects.get(pk=id)

        context = {
            "id":id,
            "survey_source": json.dumps(survey.jsontext),
            "survey":survey
        }

        return render(request, self.template_name, context)

class FormulirElektronikResultView(SurveyBaseView, View):
    template_name = "formulir_elektronik/result.html"
    def get(self, request, id):
        results = models.survey_result.objects.filter(survey_id=id).values('hasil')
        survey = models.survey.objects.get(pk=id)
        survey_title = models.survey.objects.values_list('judul', flat=True).get(pk=id)
        context = {
            'id': id,
            'survey_title': survey_title,
            'survey_source': json.dumps(survey.jsontext),
            'survey_result': json.dumps(list(results))
        }
        return render(request, self.template_name, context)

class FormulirElektronikViewView(SurveyBaseView, View):
    template_name = "formulir_elektronik/view.html"

    def get(self, request, slug, *args, **kwargs):
        user_id = request.user.id

        survey = models.survey.objects.filter(kode=slug)
        for survey in survey:
            survey.respondents = models.survey_result.objects.filter(survey=survey).count()

        context = {
            "id":survey.id,
            "survey_source": json.dumps(survey.jsontext),
            "survey":survey,
            "user_id":user_id
        }

        return render(request, self.template_name, context)

# PSM
class SKMTesUrineView(SurveyBaseView, View):
    template_name = "psm/skm_tes_urine/skm_tes_urine.html"

    def get(self, request):
        tipe_survei = TipeSurvei.objects.get(nama="SKM Tes Urine")

        daftar_pertanyaan = [pertanyaan['pertanyaan'] for pertanyaan in tipe_survei.daftar_pertanyaan]

        list_survei = DataSurvei.objects.filter(tipe=tipe_survei.id)

        context = {
            'list_survei': list_survei,
            'tipe_survei': tipe_survei.id,
            'daftar_pertanyaan': json.dumps(daftar_pertanyaan),
            'daftar_satker': Satker.objects.all()
        }

        return render(request, self.template_name, context)

# Dayatif
class SKMLifeSkill(SurveyBaseView, View):
    template_name = "dayatif/skm_life_skill/skm_life_skill.html"

    def get(self, request):
        tipe_survei = TipeSurvei.objects.get(nama="SKM Life Skill")

        daftar_pertanyaan = [pertanyaan['pertanyaan'] for pertanyaan in tipe_survei.daftar_pertanyaan]

        list_survei = DataSurvei.objects.filter(tipe=tipe_survei.id)

        context = {
            'list_survei': list_survei,
            'tipe_survei': tipe_survei.id,
            'daftar_pertanyaan': json.dumps(daftar_pertanyaan),
            'daftar_satker': Satker.objects.all()
        }

        return render(request, self.template_name, context)

class KeberhasilanKewirausahaanView(SurveyBaseView, View):
    template_name = "dayatif/keberhasilan_kewirausahaan/keberhasilan_kewirausahaan.html"

    def get(self, request):
        tipe_survei = TipeSurvei.objects.get(nama="Keberhasilan dan Kewirausahaan")

        daftar_pertanyaan = [pertanyaan['pertanyaan'] for pertanyaan in tipe_survei.daftar_pertanyaan]

        list_survei = DataSurvei.objects.filter(tipe=tipe_survei.id)

        context = {
            'list_survei': list_survei,
            'tipe_survei': tipe_survei.id,
            'daftar_pertanyaan': json.dumps(daftar_pertanyaan),
            'daftar_satker': Satker.objects.all()
        }

        return render(request, self.template_name, context)

class SurveiIKRNView(SurveyBaseView, generic.TemplateView):
    template_name = "dayatif/survei_ikrn/survei_ikrn.html"

class SurveiIKRNCreateView(SurveyBaseView, generic.TemplateView):
    template_name = "dayatif/survei_ikrn/create.html"

class SurveiIKRNDetailView(SurveyBaseView, generic.TemplateView):
    template_name = "dayatif/survei_ikrn/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = TipeSurvei.objects.get(pk=context['id'])
        context['nama'] = data.nama
        context['rawjson'] = json.dumps(data.daftar_pertanyaan)
        return context

class SurveiIKRNEditView(SurveyBaseView, generic.TemplateView):
    template_name = "dayatif/survei_ikrn/edit.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = TipeSurvei.objects.get(pk=context['id'])
        context['nama'] = data.nama
        context['rawjson'] = json.dumps(data.daftar_pertanyaan)
        return context