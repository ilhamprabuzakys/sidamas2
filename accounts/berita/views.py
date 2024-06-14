from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
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

class BeritaBaseView(GlobalPermissionMixin, LoginRequiredMixin):
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class BeritaListView(BeritaBaseView, View):
    template_name = "berita/list_berita.html"
    
    def get(self, request):
        context = {
            "list_berita" : models.Berita.objects.all()
        }
        return render(request, self.template_name, context)

class BeritaCreateView(BeritaBaseView, View):
    template_name = "berita/create_berita.html"
    
    def get(self, request):
        form = forms.BeritaForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the form data to the database
            instance = form.save(commit=False)
            instance.dibuat_oleh = request.user  # Assuming you have authentication in place
            instance.save()
            return redirect('success_url')  # Redirect to a success page
        else:
            form = forms.BeritaForm()
        
        context = { "form" : form }
            
        return render(request, self.template_name, context)
    
        
class BeritaDetailView(View):
    def get(self, request, pk):
        return redirect(reverse('home:detail_berita', pk))

class kategoriListView(generic.ListView):
    model = models.Kategori
    form_class = forms.KategoriForm

class kategoriCreateView(generic.CreateView):
    model = models.Kategori
    form_class = forms.KategoriForm


class kategoriDetailView(generic.DetailView):
    model = models.Kategori
    form_class = forms.KategoriForm


class kategoriUpdateView(generic.UpdateView):
    model = models.Kategori
    form_class = forms.KategoriForm
    pk_url_kwarg = "pk"


class kategoriDeleteView(generic.DeleteView):
    model = models.Kategori
    success_url = reverse_lazy("berita_kategori_list")


class beritaListView(generic.ListView):
    model = models.Berita
    form_class = forms.BeritaForm


class beritaCreateView(generic.CreateView):
    model = models.Berita
    form_class = forms.BeritaForm


class beritaDetailView(generic.DetailView):
    model = models.Berita
    form_class = forms.BeritaForm


class beritaUpdateView(generic.UpdateView):
    model = models.Berita
    form_class = forms.BeritaForm
    pk_url_kwarg = "pk"


class beritaDeleteView(generic.DeleteView):
    model = models.Berita
    success_url = reverse_lazy("berita_berita_list")
