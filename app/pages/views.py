from django.db.models import query
from django.views import generic
from django.views.generic import TemplateView
from .forms import ImageForm
from .models import Image
from django.shortcuts import reverse


class HomePageView(generic.CreateView):
    template_name = 'home.html'
    form_class = ImageForm
    
    def get_success_url(self):
        if self.object.rekognition_type == 'FACE':
        # redirect to "/faces" after uploading image
            return reverse('face_list')
    
    def form_valid(self,form):
        # assign current user to image for image ownership
        image = form.save(commit = False)
        image.user = self.request.user
        # image.save()
        return super().form_valid(form)
