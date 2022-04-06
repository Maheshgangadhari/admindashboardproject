from ckeditor.fields import RichTextField
from django.db import models

from django.contrib.auth import get_user_model
User = get_user_model()


# Create your models here.

# ====================wallet module=======================
# only display values
class allTransactions(models.Model):
    alltrans = [
        ('Trash', 'Trash'),
        ('In Wallet', 'In Wallet'),
        ('On Hold', 'On Hold'),
        ('Request Sent', 'Request Sent'),
        ('Accept', 'Accept'),
    ]
    wpaid = [
        ('Unpaid', 'Unpaid'),
        ('Received', 'Received'),
        ('Paid', 'Paid')
    ]
    Date = models.DateTimeField()
    CampaignOwner = models.CharField(max_length=100)
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Campaign = models.CharField(max_length=200)
    Commission = models.PositiveBigIntegerField()
    IntegrationCode = models.TextField(max_length=500)
    wStatus = models.CharField(max_length=200, choices=alltrans)
    wPaid = models.CharField(max_length=200, choices=wpaid)


#   Withdraw Requests
class WithdrawRequests(models.Model):
    # RequestID
    withdraw = [
        ('Paid', 'Paid'),
        ('Received', 'Received')
    ]
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Date = models.DateField()
    PaymentMethod = models.CharField(max_length=100)
    TransactionsIds = models.PositiveIntegerField()
    Total = models.BigIntegerField()
    withdrawStatus = models.CharField(max_length=200)


# payments
# only display
class Payments(models.Model):
    pay_status = [
        ('Enabled', 'Enabled'),
        ('Disabled', 'Disabled')
    ]
    paymentmethod = models.CharField(max_length=500)
    pstatus = models.CharField(max_length=100, choices=pay_status)


# wallet settings
class Walletsettings(models.Model):
    wsettings = [
        ('On Hold', 'On Hold'),
        ('In Wallet', 'In Wallet')
    ]
    DefaultExternalOrderStatus = [
        ('On Hold', 'On Hold'),
        ('In Wallet', 'In Wallet')
    ]
    defaultactionstatus = models.CharField(max_length=100, choices=wsettings)
    defaultExternalOrderstatus = models.CharField(max_length=100, choices=DefaultExternalOrderStatus)
    Minimumwithdrawamount = models.PositiveIntegerField()
    # post like
    Withdrawwarningmessage=RichTextField()

