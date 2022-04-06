from django.db import models

# Create your models here.

from django.contrib.auth import get_user_model
User = get_user_model()


# =================activity=======================================================
# system orders
class SyetemOrders(models.Model):
    order_status_choice = [
        ('Complete', 'Complete'),
        ('Processed', 'Processed'),
    ]
    orderid = models.IntegerField()
    total = models.PositiveIntegerField()
    country = models.GenericIPAddressField()
    store = models.ImageField(upload_to='system_store')
    status = models.CharField(max_length=100, choices=order_status_choice)
    commission = models.CharField(max_length=200)
    systemorderdate = models.DateTimeField()

    class Meta:
        verbose_name_plural = "System Orders"
class SystemLogs(models.Model):
    clickid = models.PositiveIntegerField()
    website = models.CharField(max_length=300)
    ip = models.GenericIPAddressField()
    CreatedAt = models.DateTimeField(auto_created=True)
    ClickType = models.CharField(max_length=400)
    CustomData = models.CharField(max_length=500)

    class Meta:
        verbose_name_plural = "System Logs"
class SystemReport(models.Model):
    Username = models.ForeignKey(User, on_delete=models.CASCADE)
    # user id and user name
    affilatename = models.CharField(max_length=200)
    country = models.ImageField(upload_to='countryreportsystem')
    clickcount = models.IntegerField()
    clickcommission = models.BigIntegerField()
    salecount = models.IntegerField()
    salecommission = models.BigIntegerField()
    cpa = models.CharField(max_length=200)
    totalincome = models.BigIntegerField()
    totalcommission = models.BigIntegerField()


    class Meta:
        verbose_name_plural = "System Report"


# show details only
class walletreport(models.Model):
    walletchoice = [
        ('InWallet', 'InWallet'),
        ('Onhold', 'Onhold'),
        ('Accept', 'Accept')
    ]
    Username = models.ForeignKey(User, on_delete=models.CASCADE)
    Commission = models.BigIntegerField()
    From = models.CharField(max_length=200)
    Type = models.CharField(max_length=200)
    OrderTotal = models.CharField(max_length=100)
    PaymentMethod = models.CharField(max_length=200)
    Comment = models.CharField(max_length=100)
    walletstatus = models.CharField(max_length=200, choices=walletchoice)
    walletdate = models.DateTimeField(auto_created=True)


    class Meta:
        verbose_name_plural = "Wallet Report"
