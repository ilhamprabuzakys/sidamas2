from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse

from .api_dayatif import *
from .api_psm import *

@api_view(['GET'])
def api_root(request, format=None):
    base_url = request.build_absolute_uri('/')
    
    return Response({
        'PSM': f"{base_url}kegiatan/api/v1/psm/",
        'DAYATIF': f"{base_url}kegiatan/api/v1/dayatif/"
    })