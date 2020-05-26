from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.

from .models import User

class UserResource(resources.ModelResource):
    class Meta:
        model = User


@admin.register(User)
class UserAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'password',)
    list_filter = ('id', 'name', 'password',)

