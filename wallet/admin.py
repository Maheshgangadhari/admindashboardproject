from django.contrib import admin
from wallet.models import *
# Register your models here.
admin.site.register(allTransactions)
admin.site.register(Walletsettings)
admin.site.register(Payments)
admin.site.register(WithdrawRequests)