from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import UserProfileChangeForm, UserProfileCreationForm

UserProfile = get_user_model()


class UserProfileAdmin(UserAdmin):
    add_form = UserProfileCreationForm
    form = UserProfileChangeForm
    model = UserProfile
    list_display = ['email', 'username', 'first_name', 'last_name']

admin.site.register(UserProfile, UserProfileAdmin)
