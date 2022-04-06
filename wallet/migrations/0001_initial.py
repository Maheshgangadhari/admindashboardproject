# Generated by Django 4.0.3 on 2022-03-27 07:45

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paymentmethod', models.CharField(max_length=500)),
                ('pstatus', models.CharField(choices=[('Enabled', 'Enabled'), ('Disabled', 'Disabled')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Walletsettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('defaultactionstatus', models.CharField(choices=[('On Hold', 'On Hold'), ('In Wallet', 'In Wallet')], max_length=100)),
                ('defaultExternalOrderstatus', models.CharField(choices=[('On Hold', 'On Hold'), ('In Wallet', 'In Wallet')], max_length=100)),
                ('Minimumwithdrawamount', models.PositiveIntegerField()),
                ('Withdrawwarningmessage', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='WithdrawRequests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField()),
                ('PaymentMethod', models.CharField(max_length=100)),
                ('TransactionsIds', models.PositiveIntegerField()),
                ('Total', models.BigIntegerField()),
                ('withdrawStatus', models.CharField(max_length=200)),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='allTransactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateTimeField()),
                ('CampaignOwner', models.CharField(max_length=100)),
                ('Campaign', models.CharField(max_length=200)),
                ('Commission', models.PositiveBigIntegerField()),
                ('IntegrationCode', models.TextField(max_length=500)),
                ('wStatus', models.CharField(choices=[('Trash', 'Trash'), ('In Wallet', 'In Wallet'), ('On Hold', 'On Hold'), ('Request Sent', 'Request Sent'), ('Accept', 'Accept')], max_length=200)),
                ('wPaid', models.CharField(choices=[('Unpaid', 'Unpaid'), ('Received', 'Received'), ('Paid', 'Paid')], max_length=200)),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]