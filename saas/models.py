from django.db import models

# Create your models here.

from django.contrib.auth import get_user_model
User = get_user_model()
# ====================saas===========
# vendormarket tools1
class VendorMarketTools(models.Model):
    vendor_choice = [
        ('Enable', 'Enable'),
        ('Disable', 'Disable'),
    ]
    commission_type_choice = [
        ('Select Product Commission Type', 'Select Product Commission Type'),
        ('Percentage(%)', 'Percentage(%)'),
        ('Fixed', 'Fixed '),
    ]
    click_choice = [
        ('Allow Single Click', 'Allow Single Click'),
        ('Allow Multi Click', 'Allow Multi Click'),
    ]
    clickstatus_choice = [
        ('Enable', 'Enable'),
        ('Disable', 'Disable'),
    ]
    status = models.CharField(max_length=20,
                              choices=vendor_choice,
                              default='Enable'
                              )

    clcikstatus = models.CharField(max_length=20,
                                   choices=clickstatus_choice,
                                   default='Enable'
                                   )
    noofclick = models.IntegerField()
    amountperclick = models.FloatField()

    #     admin sale commission from vendors
    commissiontype = models.CharField(max_length=30,
                                      choices=commission_type_choice,
                                      default='Enable'
                                      )
    #     admin click commission from vendors
    clikcallow = models.CharField(max_length=20, choices=click_choice)


# vendor store module
class Vendorstore(models.Model):
    vsalecom = [
        ('Percentage', 'Percentage'),
        ('Fixed', 'Fixed')

    ]
    vstatus_choice = [
        ('Enable', 'Enable'),
        ('Disable', 'Disable'),
    ]
    Vstatus = models.CharField(max_length=20,
                               choices=vstatus_choice,
                               default='Enable'
                               )

    vclickcommission = models.IntegerField()
    vclickrupees = models.FloatField()
    vsalerupees = models.FloatField()
    vsalecommission = models.CharField(max_length=20, choices=vsalecom)


class VendorDeposit(models.Model):
    depostatus_choice = [
        ('Enable', 'Enable'),
        ('Disable', 'Disable'),
    ]
    vdstatus = models.CharField(max_length=20,
                                choices=depostatus_choice,
                                default='Enable'
                                )

    vminimumdeposit = models.FloatField()


class VendorPermissions(models.Model):
    vnp_choice = [
        ('No need admin aprroval', 'No need admin aprroval'),
        ('need admin aprroval', 'need admin aprroval'),

    ]
    vnc_choice = [
        ('No need admin aprroval', 'No need admin aprroval'),
        ('need admin aprroval', 'need admin aprroval'),

    ]
    vns_choice = [
        ('No need admin aprroval', 'No need admin aprroval'),
        ('need admin aprroval', 'need admin aprroval'),

    ]
    veo_choice = [
        ('No need admin aprroval', 'No need admin aprroval'),
        ('need admin aprroval', 'need admin aprroval'),

    ]
    vac_choice = [
        ('No need admin aprroval', 'No need admin aprroval'),
        ('need admin aprroval', 'need admin aprroval'),

    ]
    vcc_choice = [
        ('No need admin aprroval', 'No need admin aprroval'),
        ('need admin aprroval', 'need admin aprroval'),

    ]

    vnp = models.CharField(max_length=28, choices=vnp_choice)
    vnc = models.CharField(max_length=28, choices=vnc_choice)
    vns = models.CharField(max_length=28, choices=vns_choice)
    veo = models.CharField(max_length=28, choices=veo_choice)
    vac = models.CharField(max_length=28, choices=vac_choice)
    vcc = models.CharField(max_length=28, choices=vcc_choice)


# transactions saas
class Transactionssaas(models.Model):
    # Id

    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Date = models.DateField()
    PaymentMethod = models.CharField(max_length=200)
    # TransactionsIds
    Total = models.BigIntegerField()
    tStatus = models.CharField(max_length=200)


class CustomStatusHistory(models.Model):
    cstatus = models.CharField(max_length=200)
    comments = models.CharField(max_length=300)



