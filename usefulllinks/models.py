from django.db import models

# Create your models here.
# from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
from django.db import models

from django.utils import timezone
from datetime import timedelta
from django.conf import settings

# usefull links
# Create your models here.
class AwardLevel(models.Model):
    levelnumber = models.CharField(max_length=100)
    jumplevel = models.CharField(max_length=100)
    minimumearning = models.IntegerField()
    salecomissionrate = models.IntegerField()
    bonus = models.IntegerField()
    Defaultregistrationlevel = models.BooleanField(default=False)
#
#
# # lanaguiages
class Language(models.Model):
    Flag = models.ImageField(upload_to='uploads/')
    Name = models.CharField(max_length=200)
    TranslationMissingAll = models.CharField(max_length=200)
    IsDefault = models.BooleanField(default=False)
    Status = models.BooleanField(default=False)
#
#
# # Currencies
class Currencies(models.Model):
    status_choice = [
        ('0', 'Enable'),
        ('1', 'Disable'),
    ]

    CurrencyType = models.CharField(max_length=100)
    SymbolRight = models.CharField(max_length=100,blank=True)
    SymbolLeft = models.CharField(max_length=100,null=True,blank=True)
    IsDefault = models.BooleanField(default=False)
    Status = models.CharField( max_length=20,choices=status_choice,default='1')
    Code = models.CharField(max_length=100)
    Value = models.IntegerField()
    LastUpdated = models.DateTimeField(auto_now=True)
#
#
# def get_default_date():
#     return timezone.now() + timedelta(days=settings.DAYS)
from django.utils import timezone

class SiteSetting(models.Model):
    front_status_choice = [
        ('0', 'Enable'),
        ('1', 'Disable'),
    ]
    store_status_choice = [
        ('0', 'Enable'),
        ('1', 'Disable'),
    ]

    register_form_choice = [
        ('EnableAffiliate / VendorRegistration', 'EnableAffiliate / VendorRegistration'),
        ('DisableAffiliate / VendorRegistration', 'DisableAffiliate / VendorRegistration'),
        ('Disable Affiliate Registration', 'Disable Affiliate Registration'),
        ('Disable Vendor Registration', 'Disable Vendor Registration')
    ]

    approval_status_choice = [
        ('0', 'Enable'),
        ('1', 'Disable'),
    ]
    front_lang_status_choice = [
        ('0', 'Enable'),
        ('1', 'Disable'),
    ]
    custom_logo_size_status_choice = [
        ('Enable', 'Enable'),
        ('Disable', 'Disable'),
    ]
    frontcustom_logo_size_status_choice = [
        ('Enable', 'Enaable'),
        ('Disable', 'Disable'),
    ]
    websitename = models.CharField(max_length=100)
    frontsitemaintenanceMode = models.CharField(
        max_length=20,
        choices=front_status_choice,
        default='1'
    )
    storemaintenanceMode = models.CharField(
        max_length=20,
        choices=store_status_choice,
        default='1'
    )
    Registrationform = models.CharField(
        max_length=37,
        choices=register_form_choice,
        default='1'
    )
    Approvalforregistration = models.CharField(
        max_length=37,
        choices=register_form_choice,
        default='1'
    )
    notificationemail = models.EmailField()
    SessionTimeoutTiming = models.DateTimeField()
    UserSessionTimeoutTiming = models.DateTimeField()
    FooterText = models.CharField(max_length=200)
    timezone = models.DateTimeField(default=timezone.localtime())
    FrontLanguageDropdown = models.CharField(
        max_length=20,
        choices=front_lang_status_choice,
        default='1'
    )
    hidecurrencyfrom = models.BooleanField(default=False)
    userdashboard = models.BooleanField(default=False)
    adminsidelogo = models.FileField(upload_to='adminsidelogo/')
    customlogosize = models.CharField(
        max_length=20,
        choices=custom_logo_size_status_choice,
        default='Disable'
    )
    #     height,width
    frontsidelogo = models.FileField(upload_to='frontsidelogo/')
    frontcustomlogosize = models.CharField(
        max_length=20,
        choices=frontcustom_logo_size_status_choice,
        default='Disable'
    )
    websitefavicon = models.FileField(upload_to='favicon/')
    description = models.TextField(max_length=100)
    keywords = models.TextField(max_length=100)
    author = models.CharField(max_length=100)
    googleanaliticsforsitepage = models.TextField(max_length=200)
    FaceboookPixelCode = models.TextField(max_length=200)
    FacebookChatPluginScript = models.TextField(max_length=200)

    adminside = models.BooleanField(default=False)
    affiliateside = models.BooleanField(default=False)
    storeside = models.BooleanField(default=False)
    frontside = models.BooleanField(default=False)
    globalScript = models.TextField(max_length=200)



class EmailSettings(models.Model):
    smtpcrypto_choice = [
        ('None', 'None'),
        ('TLS', 'TSL'),
        ('SSL', 'SSL'),
    ]
    mail_type_choice = [
        ('SMTP', 'SMTP'),
        ('PHP Mailer', 'PHP Mailer'),
    ]
    MailType = models.CharField(
        max_length=20,
        choices=mail_type_choice,
        default='SMTP'
    )
    FromEmail = models.EmailField()
    FromName = models.CharField(max_length=100)
    SMTPHostname = models.CharField(max_length=200)
    SMTPUsername = models.CharField(max_length=200)
    SMTPPassword = models.CharField(max_length=200)
    SMTPPort = models.PositiveIntegerField()
    SMTPCrypto = models.CharField(
        max_length=20,
        choices=mail_type_choice,
        default='None'
    )
    UnsubscribedPageTitle = models.CharField(max_length=200)
    UnsubscribedPageMessage = models.TextField(max_length=500)
    Testing = models.EmailField()


class TermsandCondition(models.Model):
    pagetitle = models.CharField(max_length=200)
    # blog like
    pagecontent = RichTextField()

#
class TrackingCokkies(models.Model):
    affilate_tracking_choice = [
        ('Select', 'Select'),
        ('Use Cookies', 'Use Cookies'),
        ('Use Local Storaqge', 'Use Local Storaqge'),
        ('Use Cookies & Use Local Storaqge', 'Use Cookies & Use Local Storaqge'),
    ]

    CookiesTracker = [
        ('Enable', 'Enable'),
        ('Disable', 'Disable'),
    ]

    affilateTracking = models.CharField(
        max_length=32,
        choices=affilate_tracking_choice,
        default='Select'
    )
    BlockClikAcrossBrowsers = models.CharField(
        max_length=20,
        choices=CookiesTracker,
        default='Disable'
    )


class GoogleRecaptcha(models.Model):
    Adminlogin = [
        ('Enable', 'Enable'),
        ('Disable', 'Disable'),
    ]
    Affiliatelogin = [
        ('Enable', 'Enable'),
        ('Disable', 'Disable'),
    ]
    AffiliateRegister = [
        ('Enable', 'Enable'),
        ('Disable', 'Disable'),
    ]
    Clientlogin = [
        ('Enable', 'Enable'),
        ('Disable', 'Disable'),
    ]
    ClientRegister = [
        ('Enable', 'Enable'),
        ('Disable', 'Disable'),
    ]

    sitekey = models.CharField(max_length=300)
    secretkey = models.CharField(max_length=300)
    adminlogin = models.CharField(
        max_length=20,
        choices=Adminlogin,
        default='Disable'
    )
    affilatelogin = models.CharField(
        max_length=20,
        choices=Adminlogin,
        default='Disable'
    )
    affilateregister = models.CharField(
        max_length=20,
        choices=AffiliateRegister,
        default='Disable'
    )
    clientregister = models.CharField(
        max_length=20,
        choices=ClientRegister,
        default='Disable'
    )
    clientlogin = models.CharField(
        max_length=20,
        choices=Clientlogin,
        default='Disable'
    )


class UserDashboard(models.Model):
    top_affilate = [
        ('Enable', 'Enable'),
        ('Disable', 'Disable'),
    ]
    topaffilate = models.CharField(
        max_length=20,
        choices=top_affilate,
        default='Disable'
    )

