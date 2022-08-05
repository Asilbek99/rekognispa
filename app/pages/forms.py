from django.contrib.auth import get_user_model
from django import forms
from .models import Image

UserProfile = get_user_model()


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('title', 'image', 'rekognition_type')
        
    def __init__(self, *args, **kwargs):
        super(ImageForm, self).__init__(*args, **kwargs)
        # self.fields('image').label = ''
        for visible in self.visible_fields():
            # setting tag values for image tag in add record page
            if visible.name == 'image':
                visible.field.widget.attrs['onchange'] = 'readURL(this)'
                visible.field.widget.attrs['hidden'] = ''
