from typing import Any
from django.conf import settings
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.http.request import HttpRequest
import requests
import json
from users.models import Profile

"""
    Keterangan User di SIDAMAS (Updated 19 January 2024)
    Admin : is_staff True
    SuperAdmin : is_staff True is_superuser True
    Pegawai : is_staff False is_superuser False
"""

class SidamasLDAPBackend(BaseBackend):
    def check_login(self,user_id, password):
        #url = "http://sso.bnn.go.id/ldap/auth/login"; kalau sudah di dalam intranet
        url = "https://sidepe.bnn.go.id/api/Publik/login_sso/"
        req = requests.post(url, data=json.dumps({'identity':user_id, 'password':password}), headers={'Accept': 'application/json'})
        retval = json.loads(req.text)
        if retval['auth_status'] == "1000" or retval['auth_status'] == "0300" or retval['auth_status'] == "0100":
            return True
        else:
            return False

    # kalau auth_status=="1000", berarti dia punya NIP di Simpeg
    # kalau auth_status=="0300", berarti login gagal
    # kalau auth_status=="0100", login berhasil dan ada email simpeg-nya
    # jadi login berhasil kalau auth_status = 0100 atau 1000

    def authenticate(self, request, username=None, password=None):
        login_valid = self.check_login(username, password)
        if login_valid:
            print("login valid")
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                user = User(username=username)
                user.set_password(password)
                user.is_staff = False
                user.is_superuser = False
                user.save()
                profile = Profile.objects.get_or_create(user=user)
                if profile:
                    return user
        else:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

    # def check_login(self, user_id, password):
    #     # url = "http://sso.bnn.go.id/ldap/auth/login";
    #     url = "https://sidepe.bnn.go.id/api/Publik/login_sso/"
    #     req = Request('POST', url, data={'username': user_id, 'password': password}, headers={
    #                   'Accept': 'application/json'})
    #     print(req.text)
    #     retval = json.loads(req.text)
    #     if retval.auth_status == "1000" or retval.auth_status == "0300":
    #         return True
    #     else:
    #         return False
