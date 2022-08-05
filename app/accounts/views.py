from django.urls import reverse_lazy
from django.views import generic
from .forms import UserProfileCreationForm
    
class SignUpView(generic.CreateView):
    form_class = UserProfileCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
