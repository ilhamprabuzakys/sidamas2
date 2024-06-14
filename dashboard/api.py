from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import Satker, Profile
from users.serializers import ProfileSerializer

class UpdateProfileInformationViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    # def list(self, request):
    #     user = self.request.user
    #     user_profil = self.request.user.profile

    #     if user_profil is None:
    #         return Response({'detail': 'User belum memiliki profil'}, status=status.HTTP_400_BAD_REQUEST)
    #     else:
    #         return Response({'detail': 'Profil user : ' + user.first_name}, status=status.HTTP_200_OK)

    # def create(self, request):
        # try:
        #     data = request.data
        #     user = self.request.user
        #     user_profile = self.request.user.profile
            
        #     print('Data yang diterima:', data)

        #     data_first_name = data.get('first_name')
        #     data_last_name = data.get('last_name')
        #     data_satker = data.get('satker')
        #     data_direktorat = data.get("direktorat")

        #     if data is not None:
        #         user.first_name = data_first_name
        #         user.last_name = data_last_name
        #         user.save()
                
        #         satker_instance = get_object_or_404(Satker, nama_satker=data_satker)
        #         user_profile.satker = satker_instance
        #         user_profile.direktorat = data_direktorat
        #         user_profile.save()
                
        #         print('Memperbarui data profile user:')
        #     else:
        #         print('Data yang dikirimkan kosong ...', data)

        #     print('Data profil user yang terbaru : ',
        #           user)

        #     return Response({'success': True, 'data': user_profile}, status=status.HTTP_200_OK)
        # except Exception as e:
        #     print('Error:', str(e))
        #     return Response({'success': False, 'error': 'An error occurred'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)