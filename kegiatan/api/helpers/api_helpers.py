from django_filters.rest_framework import DjangoFilterBackend
from openpyxl import Workbook
from openpyxl.styles import alignment
from openpyxl.utils import get_column_letter, column_index_from_string

from rest_framework import status, viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from users.models import Profile, Satker

from django.db.models import Count, Q

import openpyxl
from openpyxl.styles import Alignment
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.table import Table, TableStyleInfo

import re
import os
import codecs
import shutil
import datetime
import calendar
import pandas as pd
from django.conf import settings

from sidamas import pagination

from kegiatan import models
from kegiatan.api import serializers
from kegiatan.api import filters
from users.serializers import SatkerSerializer
from users.models import Satker


# =============================================
# ACTION GENERIC HELPERS
# =============================================

# ======= LISTING DATA =======
def get_data_list(request, origin_queryset, serializer_class):
    queryset = origin_queryset.filter(satker__parent__isnull=True).order_by('satker__satker_order', 'tanggal_awal').distinct('satker__satker_order')
    queryset = get_data_list_queryset(request, queryset)

    paginator = pagination.Page10NumberPagination()
    paginated_queryset = paginator.paginate_queryset(queryset, request)

    serializer = serializer_class(paginated_queryset, many=True, context={'request': request})

    return paginator.get_paginated_response(serializer.data)

def get_data_list_bnnk(satker, model_class, serializer_class):
    data = model_class.objects.all().filter(satker_id=satker, satker__level=1).order_by('satker__nama_satker')

    serialized_data = [{
        'satker': SatkerSerializer(satker, many=False).data,
        'data': serializer_class(data, many=True).data
    }]

    return Response(serialized_data, status=status.HTTP_200_OK)

def get_data_list_dukungan(request, origin_queryset, serializer_class):
    queryset = origin_queryset.filter(satker__parent__isnull=True).order_by('satker__satker_order').distinct('satker__satker_order')
    queryset = get_data_list_queryset(request, queryset)

    paginator = pagination.Page10NumberPagination()
    paginated_queryset = paginator.paginate_queryset(queryset, request)

    serializer = serializer_class(paginated_queryset, many=True, context={'request': request})

    return paginator.get_paginated_response(serializer.data)
# =======/ LISTING DATA /=======

def kirim_kegiatan_helper(model_class, request):
    kegiatan_id = request.data.get("kegiatan_id", None)
    kegiatan_id = int(kegiatan_id) if kegiatan_id else kegiatan_id
    satker = request.user.profile.satker
    parent = get_keterangan_pengiriman(satker)

    try:
        kegiatan = model_class.objects.filter(pk=kegiatan_id).first()
        kegiatan.status = get_status_pengiriman(satker.level)
        kegiatan.save()

        return Response({
            'status': True,
            'message': f'Data kegiatan ID {kegiatan_id} dari Satuan Kerja {satker.nama_satker} berhasil dikirim ke {parent.get("keterangan")}',
            'parent': parent,
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            'status': False,
            'message': f'Gagal mengirim kegiatan ID {kegiatan_id} dari Satuan Kerja ID {satker.pk}',
            'kegiatan_id': kegiatan_id,
            'error': f'{str(e)}'
        }, status=status.HTTP_400_BAD_REQUEST)

def delete_all_kegiatan_helper(model_class, pk):
    try:
        deleted_count, _ = model_class.objects.filter(satker_id=pk).delete()

        return Response({
            'status': deleted_count > 0,
            'deleted_count' : deleted_count,
            'message': 'Data kegiatan berhasil dihapus' if deleted_count > 0 else f'Data kegiatan dari Satker ID-{pk} tidak ditemukan',
            'satker_id': pk,
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            'status': False,
            'message': f'Gagal saat menghapus semua kegiatan pada Satker ID-{pk}',
            'satker_id': pk,
            'error': f'{str(e)}'
        }, status=status.HTTP_400_BAD_REQUEST)

def aksi_semua_kegiatan(request, model_class):
    tipe = request.data.get("tipe", 'kirim')
    satker_id = request.data.get("satker_id", None)
    nama_satker = request.data.get("nama_satker", None)

    try:
        satker_instance = Satker.objects.filter(nama_satker=nama_satker).first() if not satker_id else Satker.objects.filter(pk=satker_id).first()
        satker_parent = {}

        if satker_instance.level == 1:
            satker_parent_instance = satker_instance.parent
            satker_parent['id'] = satker_parent_instance.pk
            satker_parent['keterangan'] = satker_parent_instance.nama_satker
        elif satker_instance.level == 0:
            satker_parent['id'] = 213
            satker_parent['keterangan'] = 'BNN Pusat'
        else:
            satker_parent['id'] = 0
            satker_parent['keterangan'] = ''

        kegiatan = model_class.objects.filter(satker_id=satker_instance.pk)
        message = ''

        if tipe == 'kirim':
            if satker_instance.level == 0:
                kegiatan.update(status=2)
            elif satker_instance.level == 1:
                kegiatan.update(status=1)

            message = f'Data kegiatan dari Satuan Kerja {satker_instance.nama_satker} berhasil dikirim ke {satker_parent.get("keterangan")}'
        else:
            if satker_instance.level == 0:
                kegiatan.update(status=1)
            elif satker_instance.level == 1:
                kegiatan.update(status=0)

            message = f'Data kegiatan dari Satuan Kerja {satker_instance.nama_satker} berhasil dibatalkan dikirim ke {satker_parent.get("keterangan")}'

        return Response({
            'status': True,
            'message': message,
            'parent': satker_parent,
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            'status': False,
            'message': f'Gagal melakukan proses kirim/batal dari Satuan Kerja {nama_satker or satker_id}',
            'satker': nama_satker or satker_id,
            'error': f'{str(e)}'
        }, status=status.HTTP_400_BAD_REQUEST)


# =============================================
# EXPORTING DATA
# =============================================

def get_export_file_name(satker_level, satker_nama, rentang_waktu, main_name):
    tahun = datetime.datetime.now().year
    today = datetime.date.today()
    start_of_week = today - datetime.timedelta(days=today.weekday())
    end_of_week = start_of_week + datetime.timedelta(days=6)

    if satker_level != 2:
        if rentang_waktu == 'semua':
            file_name = f'{main_name} {satker_nama} TAHUN {tahun}'
        elif rentang_waktu == 'triwulan1':
            file_name = f'{main_name} {satker_nama} TRIWULAN 1 (Januari - Maret) TAHUN {tahun}'
        elif rentang_waktu == 'triwulan2':
            file_name = f'{main_name} {satker_nama} TRIWULAN 2 (April - Juni) TAHUN {tahun}'
        elif rentang_waktu == 'triwulan3':
            file_name = f'{main_name} {satker_nama} TRIWULAN 3 (July - September) TAHUN {tahun}'
        elif rentang_waktu == 'triwulan4':
            file_name = f'{main_name} {satker_nama} TRIWULAN 4 (Oktober - Desember) TAHUN {tahun}'
        elif rentang_waktu == 'hari_ini':
            file_name = f'{main_name} {satker_nama} TANGGAL {today.strftime("%d %B %Y")}'
        elif rentang_waktu == 'minggu_ini':
            file_name = f'{main_name} {satker_nama} MINGGU INI ({start_of_week.strftime("%d %B %Y")} - {end_of_week.strftime("%d %B %Y")})'
        elif rentang_waktu == 'bulan_ini':
            file_name = f'{main_name} {satker_nama} TANGGAL {today.strftime("%B %Y")}'
    else:
        file_name = f'{main_name} BNNK & BNNP TAHUN {tahun}'

    return file_name


# =============================================
# UTILS HELPERS
# =============================================

# KIRIM KEGIATAN HELPERS
def get_keterangan_pengiriman(satker):
    parent = {}

    if satker.level == 1: # BNNK
        # parent_instance = satker.parent
        # parent['id'] = parent_instance.pk
        # parent['keterangan'] = parent_instance.nama_satker
        parent['id'] = 213
        parent['keterangan'] = 'BNN Pusat'
    elif satker.level == 0: # BNNP
        parent['id'] = 213
        parent['keterangan'] = 'BNN Pusat'
    else: # PUSAT
        parent['id'] = 0
        parent['keterangan'] = ''

    return parent

def get_status_pengiriman(satker_level):
    status_map = {
        0: 2, # BNNP ke Pusat
        1: 2, # BNNK ke Pusat
    }

    status = status_map.get(satker_level, 2)

    return status

# ======= DATA =======
def get_data_list_queryset(request, queryset):
    satker = request.user.profile.satker

    if satker.level == 1:
        # BNNK
        queryset = queryset.filter(satker__id=satker, satker__level=1)
    elif satker.level == 0:
        # BNNP
        queryset = queryset.filter(satker__provinsi_id=satker.provinsi_id, status__gt=0)
    elif satker.level == 2:
        # PUSAT
        queryset = queryset.filter(status=2)
    return queryset

def get_filtered_data(satker, data, status, waktu):
    now = datetime.datetime.now()
    start_date = ''
    end_date = ''

    if waktu != 'semua':
        if waktu == 'hari_ini':
            start_date = now.replace(hour=0, minute=0, second=0, microsecond=0)
            end_date = now.replace(hour=23, minute=59, second=59, microsecond=999999)
        elif waktu == 'minggu_ini':
            start_date = now - datetime.timedelta(days=now.weekday())
            start_date = start_date.replace(hour=0, minute=0, second=0, microsecond=0)
            end_date = start_date + datetime.timedelta(days=6, hours=23, minutes=59, seconds=59, microseconds=999999)
        elif waktu == 'bulan_ini':
            start_date = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
            end_date = start_date.replace(day=calendar.monthrange(now.year, now.month)[1], hour=23, minute=59, second=59, microsecond=999999)
        elif waktu.startswith('triwulan'):
            triwulan = int(waktu[-1])
            start_month = (triwulan - 1) * 3 + 1
            start_date = now.replace(month=start_month, day=1, hour=0, minute=0, second=0, microsecond=0)
            end_month = start_month + 2
            end_date = start_date.replace(month=end_month, day=calendar.monthrange(now.year, end_month)[1], hour=23, minute=59, second=59, microsecond=999999)

            print('Triwulan :', waktu)
            print('Triwulan ke-:', triwulan)
            print('Triwulan start_month :', start_month)
            print('Triwulan start_date :', start_date)
            print('Triwulan end_month :', end_month)
            print('Triwulan end_date :', end_date)

    # return { 'start_date': start_date, 'end_date': end_date }
    print(f'Args : {waktu} {status}')

    choosen_status = 0

    if status == '1':
        if satker.level == 2:
            choosen_status = 2
        else:
            choosen_status = 1 if satker.level == 1 else 2
    else:
        choosen_status = 1 if satker.level == 0 else 0

    if waktu != 'semua':
        data = data.filter(tanggal_awal__lte=end_date, tanggal_akhir__gte=start_date)

    if status != 'semua':
        data = data.filter(status=choosen_status)

    keterangan_waktu = f'start_date {start_date} s/d end_date {end_date}' if start_date != '' else 'semua'

    print(f'Panjang data dari filter {waktu} dengan status {choosen_status} dengan waktu {keterangan_waktu}:', len(data))

    return data

def set_created_kegiatan_status(request):
    satker = request.user.profile.satker

    """
        Mapping :
        Satker Level       Status Pengiriman
        0 : BNNP        -> 1 : Sudah di BNNP
        1 : BNNK        -> 0 : Masih di BNNK
        2 : Pusat       -> 2 : Tetap di Pusat
    """

    status_map = {
        0: 1,
        1: 0,
        2: 2
    }

    status = status_map.get(satker.level, None)

    return status

def get_tanggal_kegiatan(tanggal_awal, tanggal_akhir=None):

    print('Args :', tanggal_awal, tanggal_akhir)

    start = datetime.date.fromisoformat(f'{tanggal_awal}')
    start_date = start.strftime('%-d')
    start_month = start.strftime('%B')
    start_year = start.strftime('%Y')

    nama_bulan = {
        "January": "Januari",
        "February": "Februari",
        "March": "Maret",
        "April": "April",
        "May": "Mei",
        "June": "Juni",
        "July": "Juli",
        "August": "Agustus",
        "September": "September",
        "October": "Oktober",
        "November": "November",
        "December": "Desember"
    }

    if tanggal_akhir:
        end = datetime.date.fromisoformat(f'{tanggal_akhir}')
        end_date = end.strftime('%-d')
        end_month = end.strftime('%B')
        end_year = end.strftime('%Y')

        if start_month == end_month and start_year == end_year:
            return f"{start_date} - {end_date} {nama_bulan[start_month]} {start_year}"
        elif start_year != end_year:
            return f"{start.strftime('%-d')} {nama_bulan[start_month]} {start_year} - {end.strftime('%-d')} {nama_bulan[end_month]} {end_year}"
        else:
            return f"{start.strftime('%-d')} {nama_bulan[start_month]} - {end.strftime('%-d')} {nama_bulan[end_month]} {end_year}"
    else:
        return f"{start.strftime('%-d')} {nama_bulan[start_month]} {start_year}"
