from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView


class PilihDirektoratViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        user_direktorat = request.session.get("user_direktorat")

        if user_direktorat is None:
            return Response({'detail': 'User ini belum ter-assign ke direktorat manapun'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'detail': 'User ini sudah memiliki direktorat : ' + user_direktorat}, status=status.HTTP_200_OK)

    def create(self, request):
        try:
            data = request.data
            print('Data yang diterima:', data)

            direktorat = data.get("direktorat")

            if direktorat is not None:
                self.request.session["user_direktorat"] = direktorat
                print('Memperbarui data user ke direktorat:', direktorat)
            else:
                print('Data direktorat kosong ...')

            print('Data user di akhir direktorat : ',
                  self.request.session["user_direktorat"])

            return Response({'success': True, 'direktorat': self.request.session["user_direktorat"]}, status=status.HTTP_200_OK)
        except Exception as e:
            print('Error:', str(e))
            return Response({'success': False, 'error': 'An error occurred'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



# class tbl_authViewSet(viewsets.ModelViewSet):
#     """ViewSet for the tbl_responden_survey class"""

#     queryset = models.Auth_user.objects.all()
#     serializer_class = serializers.tbl_authSerializer
#     permission_classes = [permissions.IsAuthenticated]

