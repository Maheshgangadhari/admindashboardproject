from ckeditor.fields import RichTextField
from django.db import models

# Create your models here.
# ===========marketting====================
# banner
from django.utils.safestring import mark_safe


class Categories(models.Model):
    category_choice = [
        ('Select', 'Select'),
        ('select parent category', 'select parent category'),
        ('Clicks', 'Clicks'),
        ('Salse', 'Salse'),
        ('Actions', 'Actions'),
        ('Leads', 'Leads'),
        ('Registration', 'Registration'),
        ('237606380660229', '237606380660229'),
        ('WYKR Category', 'dsd'),
        ('Programacion', 'Programacion'),
        ('Test', 'Test'),
        ('Fruit', 'Fruit'),
        ('Amall', 'Amall'),
        ('tall', 'tall'),
        ('logistics ', 'logistics '),
        ('FX', 'FX'),
        ('MD', 'MD'),
        ('Puzzle Book', 'Puzzle Book'),
        ('xxxxxx', 'xxxxxx'),
        ('E-books Delivery', 'E-books Delivery'),
        ('E test', 'E test'),
        ('Hosting', 'Hosting'),
        ('Bus', 'Bus'),
        ('Earnshow', 'Earnshow'),
        ('matrix', 'matrix'),
        ('FSL', 'FSL'),
        ('Marketing', 'Marketing'),
        ('Pintores', 'Pintores'),
        ('img', 'img'),
        ('Link', 'Link'),
        ('Husni', 'Husni'),
        ('loan', 'loan'),
        ('test', 'test'),
        ('Abbas', 'Abbas'),
        ('Lawwa Services', 'Lawwa Services'),
        ('SCKREAM Test', 'SCKREAM Test')
    ]
    Categoryname = models.CharField(max_length=200)
    parentcategory = models.CharField(max_length=200, choices=category_choice)


# Integration Tools (Banner1)
class Bannerimages(models.Model):
    image = models.ImageField(upload_to='imagebanner/')

    class Meta:
        verbose_name_plural = "Banner Images"


#  IntegrationTools


class Commonsettings(models.Model):
    Tooltypes = [
        ('Select Tool Type', 'Select Tool Type'),
        ('Sale Integration', 'Sale Integration'),
        ('Single Action Integration', 'Single Action Integration'),
        ('Multi Action Integration', 'Multi Action Integration'),
        ('Click Integration', 'Click Integration'),
    ]
    Toolperiod = [
        ('Always Running', 'Always Running'),
        ('From Today To Custom Date', 'From Today To Custom Date'),
        ('From Custom Date To Lifetime', 'From Custom Date To Lifetime'),
        ('For Custom Period', 'For Custom Period'),

    ]

    toolType = models.CharField(max_length=28, choices=Tooltypes)
    toolperiod = models.CharField(max_length=28, choices=Toolperiod)
    name = models.CharField(max_length=200)
    targetlink = models.CharField(max_length=500)
    categorie = models.ForeignKey(Categories, on_delete=models.CASCADE)
    featuredimage = models.FileField(upload_to='featureimagebanner/')
    # Afflow_for_affiliatechoice = [
    #     ('All', 'All'),
    #     ('Selected Groups ', 'Selected Groups'),
    #     ('Selected Affiliate', 'Selected Affiliate'),
    #
    # ]
    # Afflowforaffiliate= models.CharField(max_length=20,
    #                           choices=Afflow_for_affiliatechoice,
    #                           default='All'
    #               )

    is_draft = models.BooleanField(default=False)
    is_public = models.BooleanField(default=False)

    class Meta:
        abstract = True


class LinkaddsSettings(Commonsettings):
    linktitle = models.CharField(max_length=200)


    class Meta:
        verbose_name_plural = "Link Adds Settings"


class VideeoLinkSettings(Commonsettings):
    autoplay_choice = [
        ('Disable', 'Disable'),
        ('Enable', 'Enable')
    ]
    videolink = models.CharField(max_length=200)
    autoplay = models.CharField(max_length=28, choices=autoplay_choice)
    Hegiht = models.PositiveSmallIntegerField()
    width = models.PositiveSmallIntegerField()
    buttontext = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Video Link Settings"


class GeneralSettings(Commonsettings):
    bannerimages = models.ManyToManyField(Bannerimages)
    # blog post
    terms=RichTextField()

    class Meta:
        verbose_name_plural = "General Settings"




class Levelsetting(models.Model):
    levelsettings = [
        ('Default', 'Default'),
        ('Custom', 'Custom'),
        ('Enable', 'Enable'),
    ]
    commissiontype = models.CharField(max_length=28, choices=levelsettings)
    # level-id
    CPR = models.PositiveIntegerField()
    CPS = models.PositiveIntegerField()
    CPC = models.PositiveIntegerField()
    CPA = models.PositiveIntegerField()
    # Costperregistration
    # CPS - Cost per sale
    # Percentage( %)
    # Clicks
    # Count & CPC - Cost
    # per
    # click
    # CPA - Cost
    # per
    # action

    class Meta:
        verbose_name_plural = "Level Settings"




class Recurringsetting(models.Model):
    recurringsettings = [
        ('Select Recursion', 'Select Recursion'),
        ('Every day', 'Every day'),
        ('Every week', 'Every week'),
        ('Every month', 'Every month'),
        ('Every year', 'Every year'),
        ('Custom time', 'Custom time')
    ]
    recursion = models.CharField(max_length=28, choices=recurringsettings)
    choosecustomendtime = models.DateTimeField()


    class Meta:
        verbose_name_plural = "Recurring Settings"




class Postback(models.Model):
    postbackstatus = [
        ('Default', 'Default'),
        ('Custom', 'Custom'),
        ('Enable', 'Enable'),
    ]
    postback = models.CharField(max_length=28, choices=postbackstatus)

    class Meta:
        verbose_name_plural = "Post back"




from colorfield.fields import ColorField
# Integration Tools (Text Campaigns)
class TextCampaigns(Commonsettings):
    content = models.TextField(max_length=500)
    textsize = models.PositiveSmallIntegerField()
    textcolor=ColorField(default='#FF0000')
    bordercolor=ColorField(default='#FF0000')
    backgroundcolor=ColorField(format='hexa')


#     pip install django-colorfield
from django.contrib.auth import get_user_model

User = get_user_model()


# Marketing Programs
class MarketingPrograms(models.Model):
    commission_choice = [
        ('Select Product Commission Type', 'Select Product Commission Type'),
        ('Percentage(%)', 'Percentage(%)'),
        ('Fixed', 'Fixed')
    ]
    sales_choice = [
        ('Enable', 'Enable'),
        ('Disable', 'Disable'),
    ]
    click_status_choice = [
        ('Enable', 'Enable'),
        ('Disable', 'Disable'),
    ]
    click_choice = [
        ('Allow Multi Clicks', 'Allow Multi Clicks'),
        ('Allow Single Click', 'Allow Single Click'),
    ]
    vendor=models.ForeignKey(User,on_delete=models.CASCADE)

    programname = models.CharField(max_length=200)
    commissiontype = models.CharField(max_length=100)
    commissionforsale = models.CharField(max_length=200, choices=commission_choice)
    salestatus = models.CharField(max_length=200, choices=sales_choice)
    clickallow = models.CharField(max_length=200, choices=click_choice)
    numberofclick = models.IntegerField()
    amountperclick = models.IntegerField()
    clickstatus = models.CharField(max_length=200, choices=click_status_choice)

