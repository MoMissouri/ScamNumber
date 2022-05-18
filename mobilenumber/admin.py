from django.contrib import admin
from .models import phonemodel, reviewmodel
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.
class PhonemodelResource(resources.ModelResource):

    class Meta:
        model = phonemodel
class PhoneAdmin(ImportExportModelAdmin):
    from_encoding = 'utf-8'
    # list_display= ("customer_name","customer_id", "serial_number","height","width","length", "storage_space", "weight", "storage_name", "locate", "date", "description", "quantity", "warehouse" )
    pass
admin.site.register(phonemodel, PhoneAdmin)
admin.site.register(reviewmodel)