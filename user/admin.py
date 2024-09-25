from django.contrib import admin
from .models import User
from .models import MemorialProfile
from .models import Plan
from .models import ProfilePermission
# Register your models here.

admin.site.register(User)
admin.site.register(MemorialProfile)
admin.site.register(Plan)
admin.site.register(ProfilePermission)