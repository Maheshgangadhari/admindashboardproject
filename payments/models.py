from django.db import models

# Create your models here.

class PaymentGateway(models.Model):
    store_choice = [
        ('Enable', 'Enable'),
        ('Disable', 'Disable'),
    ]
    deposit_choice = [
        ('Enable', 'Enable'),
        ('Disable', 'Disable'),
    ]
    Membership_choice = [
        ('Enable', 'Enable'),
        ('Disable', 'Disable'),
    ]
    order_choice = [
        ('Select', 'Select'),
        ('Waiting For Payment', 'Waiting For Payment'),
        ('Complete', 'Complete'),
        ('Total not match', 'Total not match'),
        ('Denied', 'Denied'),
        ('Expired', 'Expired'),
        ('Failed', 'Failed'),
        ('Pending', 'Pending'),
        ('Processed', 'Processed'),
        ('Refunded', 'Refunded'),
        ('Reversed', 'Reversed'),
        ('Voided', 'Voided'),
        ('Canceled Reversal', 'Canceled Reversal'),
    ]
    store = models.CharField(
        max_length=20,
        choices=store_choice,
        default='Disable'
    )
    Deposit = models.CharField(
        max_length=20,
        choices=deposit_choice,
        default='Disable'
    )
    Membership = models.CharField(
        max_length=20,
        choices=Membership_choice,
        default='Disable'
    )
    ShopID = models.CharField(max_length=100)
    SecretKey = models.CharField(max_length=200)

    orderstatus = models.CharField(
        max_length=20,
        choices=order_choice,
        default='Select'
    )


class CallTransactions(models.Model):
    alltrans_status_choice = [
        ('Select', 'Select'),
        ('Waiting For Payment', 'Waiting For Payment'),
        ('Complete', 'Complete'),
        ('Total not match', 'Total not match'),
        ('Denied', 'Denied'),
        ('Expired', 'Expired'),
        ('Failed', 'Failed'),
        ('Pending', 'Pending'),
        ('Processed', 'Processed'),
        ('Refunded', 'Refunded'),
        ('Reversed', 'Reversed'),
        ('Voided', 'Voided'),
        ('Canceled Reversal', 'Canceled Reversal'),
    ]
    Module = models.CharField(max_length=100)
    User = models.CharField(max_length=200)
    Price = models.BigIntegerField()
    PaymentGateway = models.CharField(max_length=200)
    # TransactionId=
    Status = models.CharField(max_length=20, choices=alltrans_status_choice, default='Select')
    Date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name='All Transactions'
        verbose_name_plural='All Transactions'
