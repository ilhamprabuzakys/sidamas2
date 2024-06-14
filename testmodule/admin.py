from django.contrib import admin
from django import forms

from . import models


class userAdminForm(forms.ModelForm):

    class Meta:
        model = models.user
        fields = "__all__"


class userAdmin(admin.ModelAdmin):
    form = userAdminForm
    list_display = [
        "created",
        "last_updated",
        "nilai",
        "pengguna",
    ]
    readonly_fields = [
        "created",
        "last_updated",
        "nilai",
        "pengguna",
    ]


#admin.site.register(models.user, userAdmin)
