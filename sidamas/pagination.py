from rest_framework.pagination import PageNumberPagination
from rest_framework_datatables.pagination import DatatablesPageNumberPagination

class Page10NumberPagination(DatatablesPageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 10

class Page100NumberPagination(DatatablesPageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 100

class Page250NumberPagination(DatatablesPageNumberPagination):
    page_size = 250
    page_size_query_param = 'page_size'
    max_page_size = 250

class Page500NumberPagination(DatatablesPageNumberPagination):
    page_size = 500
    page_size_query_param = 'page_size'
    max_page_size = 500

class Page1000NumberPagination(DatatablesPageNumberPagination):
    page_size = 1000
    page_size_query_param = 'page_size'
    max_page_size = 1000
