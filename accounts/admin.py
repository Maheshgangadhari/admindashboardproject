from django.contrib import admin

# Register your models here.

# Register your models here.
from accounts.models import CustomUser


@admin.register(CustomUser)
class CustomUser(admin.ModelAdmin):
    list_display = ['name', 'email', 'mobile', 'date_joined']

    def save_model(self, request, obj, form, change):
        obj.set_password(obj.password)
        obj.save()
        super(CustomUser, self).save_model(request, obj, form, change)



admin.site.site_header = "Affiliate Management System"
# admin.site.site_header = 'My project'                    # default: "Django Administration"
admin.site.index_title = 'Features area'                 # default: "Site administration"
admin.site.site_title = 'HTML title from adminsitration' # default: "Django site admin"


