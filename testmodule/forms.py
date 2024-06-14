from django import forms
from . import models


class userForm(forms.ModelForm):
    class Meta:
        model = models.user
        fields = [
            "nilai",
            "pengguna",
        ]
