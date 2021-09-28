from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
# Register your models here.

admin.site.register(AnonymousUser)
admin.site.register(Room)

@admin.register(UserProfile)
class UserProfileAdmin(ImportExportModelAdmin):
    pass
