from django.contrib import admin
from django.utils.html import format_html

from marketing.models import *

# Register your models here.


class BannerAdmin(admin.ModelAdmin):
    list_display = ['image_tag']

    # list_display = ['Module', 'User', 'Price', 'PaymentGateway', 'Status', 'Date']
    # list_filter = ['Module', 'User', 'Price', 'PaymentGateway', 'Status', 'Date']
    # search_fields = (
    #     'Module', 'User', 'Price', 'PaymentGateway', 'Status', 'Date'
    # )

    def image_tag(self, obj):
        return format_html('<img src="{}" />'.format(obj.image.url))

    image_tag.short_description = 'Image'
class ProgramsAdmin(admin.ModelAdmin):
    list_display = ['vendor', 'programname', 'commissiontype',
                    'commissionforsale', 'salestatus', 'clickallow', 'numberofclick', 'amountperclick', 'clickstatus', ]


    list_filter =['vendor', 'programname', 'commissiontype',
                    'commissionforsale', 'salestatus', 'clickallow', 'numberofclick', 'amountperclick', 'clickstatus', ]

    search_fields=[ 'vendor', 'programname', 'commissiontype',
                    'commissionforsale', 'salestatus', 'clickallow', 'numberofclick', 'amountperclick', 'clickstatus', ]


admin.site.register(Categories)

admin.site.register(Bannerimages,BannerAdmin)
# admin.site.register(Commonsettings)
admin.site.register(LinkaddsSettings)
admin.site.register(VideeoLinkSettings)
admin.site.register(GeneralSettings)
admin.site.register(Levelsetting)
admin.site.register(Recurringsetting)
admin.site.register(Postback)
admin.site.register(TextCampaigns)
admin.site.register(MarketingPrograms,ProgramsAdmin)
