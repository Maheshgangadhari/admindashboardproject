from django.contrib import admin
from payments.models import *
# Register your models here.

# ImportExportModelAdmin
from import_export.admin import ImportExportModelAdmin
# from django.contrib import admin
# from .models import Person

# @admin.register(Person)
class AllTransactionsAdmin(ImportExportModelAdmin):
    list_display = ['Module','User','Price','PaymentGateway','Status','Date']
    list_filter = ['Module','User','Price','PaymentGateway','Status','Date']
    search_fields = (
        'Module', 'User', 'Price', 'PaymentGateway', 'Status', 'Date'
    )


admin.site.register(PaymentGateway)
admin.site.register(CallTransactions,AllTransactionsAdmin)