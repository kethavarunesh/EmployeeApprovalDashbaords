from django.contrib import admin
from .models import Mtplnew_dataentry

class MtplnewDataEntryAdmin(admin.ModelAdmin):
    list_display = ['empcode', 'project_name', 'date', 'document_no', 'order_serial_no', 'department',
                    'material_code', 'material_description', 'supplier_name', 'qty', 'value', 'rejection_reason',
                    'reason_for_rejection', 'file_upload', 'man_hours_wasted', 'machine_hours_wasted',
                    'information_to_buyer', 'status', 'approval_comment', 'ncraised', 'remarks']
    list_filter = ['status']
    search_fields = ['empcode', 'project_name', 'document_no']

admin.site.register(Mtplnew_dataentry, MtplnewDataEntryAdmin)