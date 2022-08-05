from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

UserProfile = get_user_model()


class UserProfileCreationForm(UserCreationForm):
    class Meta:
        model = UserProfile
        fields = ('first_name', 'last_name', 'username','email')
        
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(UserCreationForm, self).__init__(*args, **kwargs)
        
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

class UserProfileChangeForm(UserChangeForm):
    class Meta:
        model = UserProfile
        fields = ('first_name', 'last_name', 'username', 'email')
        def __init__(self, *args, **kwargs):
            self.request = kwargs.pop('request', None)
            super(UserChangeForm, self).__init__(*args, **kwargs)
