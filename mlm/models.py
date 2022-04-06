from django.db import models

# Create your models here.

# mlm
# =================================================================

class MlmSettings(models.Model):
    mlmsettings = [
        ('Enable', 'Enable'),
        ('Disabled', 'Disabled'),
        ('Disable only for selected users', 'Disable only for selected users')
    ]
    mlmscriptnalStatus = [
        ('On Hold', 'On Hold'),
        ('In Wallet', 'In Wallet')
    ]
    mlmexternalStatus = [
        ('On Hold', 'On Hold'),
        ('In Wallet', 'In Wallet')
    ]
    actionreferStatus = [
        ('On Hold', 'On Hold'),
        ('In Wallet', 'In Wallet')
    ]
    showspStatus = [
        ('Show Admin As Sponser', 'Show Admin As Sponser'),
        ('Not Show', 'Not Show'),
        ('Real Sponser', 'Real Sponser')
    ]

    mlmstatus = models.CharField(max_length=200, choices=mlmsettings)
    ScriptStoreOfflinePaymentMethodReferSaleCommission = models.CharField(max_length=200, choices=mlmscriptnalStatus)
    ExternalStoreOfflinePaymentMethodReferSaleCommission = models.CharField(max_length=200, choices=mlmsettings)
    Actionrefer = models.CharField(max_length=200, choices=actionreferStatus)
    showsponser = models.CharField(max_length=200, choices=showspStatus)
    SponserName = models.CharField(max_length=200)


# mlm settings level
class Referlevel(models.Model):
    mlmcpr = models.PositiveIntegerField()
    mlmcps = models.PositiveIntegerField()
    mlmcpc = models.PositiveIntegerField()
    mlmcpa = models.PositiveIntegerField()

