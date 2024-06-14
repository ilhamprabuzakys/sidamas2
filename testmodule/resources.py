from import_export import resources, fields
from django.utils.html import format_html
from . import models


class UserResource(resources.ModelResource):
    nilai2 = fields.Field(column_name='nilaii')
    result = fields.Field(column_name='result')

    class Meta:
        model = models.user
        fields = ('nilai', 'nilai2', 'hasil', 'pengguna', 'result')

    def get_user_fields(self):
        # Extract the fields that you want to export
        return self.get_fields()

    def dehydrate_result(self, user):
        try:
            # Convert nilai and nilai2 to integers and calculate the result
            nilai = int(user.nilai) if user.nilai else 0
            nilai2 = int(user.nilai2) if user.nilai2 else 0
            return nilai - nilai2
        except (ValueError, TypeError):
            # Handle conversion errors or other issues
            return 0
        
    def dehydrate_nilai2(self, user):
        nilai2 = int(user.nilai2) if user.nilai2 else 0
        return nilai2
    

class ImageResource(resources.ModelResource):
    class Meta:
        model = models.image

    # Customize how the image field is exported
    image = fields.Field(column_name='Image')

    def dehydrate_image(self, obj):
        if obj.image:
            image_url = obj.image.url
            return format_html('<img src="{}" alt="Image">', image_url)
        return ''