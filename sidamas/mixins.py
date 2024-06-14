from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.urls import reverse

# =============================================
# GLOBALLY MIXINS PROTECTION (USER ACTIVATION)
# =============================================
class GlobalPermissionMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser == False and request.user.is_staff == False and request.user.profile.role is None or request.user.profile.satker is None or request.user.profile.is_verified == False:
            user = self.request.user
            message = "Maaf " + user.username + ", anda tidak memiliki hak akses untuk mengunjungi halaman ini."
            print(message)
            return HttpResponseRedirect(reverse("dashboard:profile"))
        return super().dispatch(request, *args, **kwargs)

# =============================================
# DIREKTORAT MIXINS LEVELING PROTECTION
# =============================================
class PsmPermissionMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser == False and request.user.profile.role != 'psm':
            user = self.request.user
            message = "Maaf " + user.username + ", anda tidak memiliki hak akses untuk mengunjungi halaman ini. Halaman ini khusus untuk direktorat Dayatif"
            print(message)
            return HttpResponseForbidden(message)
        return super().dispatch(request, *args, **kwargs)

class DayatifPermissionMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser == False and request.user.profile.role != 'dayatif':
            user = self.request.user
            message = "Maaf " + user.username + ", anda tidak memiliki hak akses untuk mengunjungi halaman ini. Halaman ini khusus untuk direktorat Dayatif"
            print(message)
            return HttpResponseForbidden(message)
        return super().dispatch(request, *args, **kwargs)

# =============================================
# SATKER LEVEL MIXINS LEVELING PROTECTION
# =============================================
class BNNPPermissionMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser == False and request.user.profile.satker.level == 1:
            user = self.request.user
            message = "Maaf " + user.username + ", anda tidak memiliki hak akses untuk mengunjungi halaman ini. Halaman ini khusus untuk BNNP"
            print(message)
            return HttpResponseForbidden(message)
        return super().dispatch(request, *args, **kwargs)