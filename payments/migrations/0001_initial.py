# Generated by Django 4.0.3 on 2022-03-29 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CallTransactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Module', models.CharField(max_length=100)),
                ('User', models.CharField(max_length=200)),
                ('Price', models.BigIntegerField()),
                ('PaymentGateway', models.CharField(max_length=200)),
                ('Status', models.CharField(choices=[('Select', 'Select'), ('Waiting For Payment', 'Waiting For Payment'), ('Complete', 'Complete'), ('Total not match', 'Total not match'), ('Denied', 'Denied'), ('Expired', 'Expired'), ('Failed', 'Failed'), ('Pending', 'Pending'), ('Processed', 'Processed'), ('Refunded', 'Refunded'), ('Reversed', 'Reversed'), ('Voided', 'Voided'), ('Canceled Reversal', 'Canceled Reversal')], default='Select', max_length=20)),
                ('Date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'All Transactions',
                'verbose_name_plural': 'All Transactions',
            },
        ),
        migrations.CreateModel(
            name='PaymentGateway',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store', models.CharField(choices=[('Enable', 'Enable'), ('Disable', 'Disable')], default='Disable', max_length=20)),
                ('Deposit', models.CharField(choices=[('Enable', 'Enable'), ('Disable', 'Disable')], default='Disable', max_length=20)),
                ('Membership', models.CharField(choices=[('Enable', 'Enable'), ('Disable', 'Disable')], default='Disable', max_length=20)),
                ('ShopID', models.CharField(max_length=100)),
                ('SecretKey', models.CharField(max_length=200)),
                ('orderstatus', models.CharField(choices=[('Select', 'Select'), ('Waiting For Payment', 'Waiting For Payment'), ('Complete', 'Complete'), ('Total not match', 'Total not match'), ('Denied', 'Denied'), ('Expired', 'Expired'), ('Failed', 'Failed'), ('Pending', 'Pending'), ('Processed', 'Processed'), ('Refunded', 'Refunded'), ('Reversed', 'Reversed'), ('Voided', 'Voided'), ('Canceled Reversal', 'Canceled Reversal')], default='Select', max_length=20)),
            ],
        ),
    ]