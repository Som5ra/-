from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.

from .models import *


class staffResource(resources.ModelResource):
    class Meta:
        model = staff


@admin.register(staff)
class staffAdmin(ImportExportModelAdmin):
    list_display = ('sid',
                    'name',
                    'sex',
                    'nation',
                    'birthday',
                    'politics',
                    'education',
                    'marriage',
                    'hometown',
                    'id_card',
                    'phone',
                    'place',
                    'home_card',
                    'c_time',
                    'num',
                    'in_time',
                    'pos',
                    'duty',
                    'pre_num',
                    'status',
                    'dep_id',
                    'account_id'
                    )
    list_filter = ('sid',
                    'name',
                    'sex',
                    'nation',
                    'birthday',
                    'politics',
                    'education',
                    'marriage',
                    'hometown',
                    'id_card',
                    'phone',
                    'place',
                    'home_card',
                    'c_time',
                    'num',
                    'in_time',
                    'pos',
                    'duty',
                    'pre_num',
                    'status',
                    'dep_id',
                    'account_id',
                   )

class depResource(resources.ModelResource):
    class Meta:
        model = department

@admin.register(department)
class depAdmin(ImportExportModelAdmin):
    list_display = (
        'did',
        'name',
        'work_id',
        'pre_dep_id',
    )
    list_filter = (
        'did',
        'name',
        'work_id',
        'pre_dep_id',
    )


admin.site.site_header = "员工管理系统"
admin.site.site_header = "员工管理系统"