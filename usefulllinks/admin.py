from django.contrib import admin

# Register your models here.
from import_export.admin import ImportExportModelAdmin
# Register your models here.
from usefulllinks.models import *



# Customize the way the admin panel looks
# class AwardAdmin(admin.ModelAdmin):
#     pass

class AwardLevelAdmin(admin.ModelAdmin):
    list_display = ['levelnumber','jumplevel','minimumearning','salecomissionrate','bonus','Defaultregistrationlevel']


class LanguageAdmin(ImportExportModelAdmin):
    list_display = ['Name','TranslationMissingAll','IsDefault','Status']
    list_filter = [
    ]
    search_fields = (

    )



class CurrencyAdmin(admin.ModelAdmin):
    list_display = ['CurrencyType','SymbolRight','SymbolLeft','IsDefault','Status','Code','Value','LastUpdated']
# Register your models here.
admin.site.register(AwardLevel,AwardLevelAdmin)
admin.site.register(Language,LanguageAdmin)
admin.site.register(Currencies,CurrencyAdmin)

admin.site.register(SiteSetting)
admin.site.register(EmailSettings)
admin.site.register(TermsandCondition)
admin.site.register(TrackingCokkies)
admin.site.register(GoogleRecaptcha)
admin.site.register(UserDashboard)

