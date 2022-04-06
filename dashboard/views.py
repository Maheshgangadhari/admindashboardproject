from django.shortcuts import render


# Create your views here.

# profile
# def Profile(request):
#     return render(request,"genral/editProfile.html")


# dash board
def dashboard(request):
    return render(request, "dashboard/dashboard.html")



# use full links
def addons(request):
    return render(request, "dashboard/addons.html")


def award(request):
    return render(request, "dashboard/award_level.html")


def affliate_theme(request):
    return render(request, "dashboard/affiliate_theme.html")


def language(request):
    return render(request, "dashboard/language.html")


def currency_list(request):
    return render(request, "dashboard/currency_list.html")


def system_status(request):
    return render(request, "dashboard/system_status.html")


def paymentset(request):
    return render(request, "dashboard/paymentsetting.html")


def all_transactions(request):
    return render(request, "payments/all_transaction.html")


def payment_gateway(request):
    return render(request, "payments/payment_gateway.html")


# marketing
def compaigns(request):
    return render(request, "marketings/integration_tools.html")


def programs(request):
    return render(request, "marketings/programs.html")


def category(request):
    return render(request, "marketings/integration_category.html")


# activity
def system_orders(request):
    return render(request, "activity/store_orders.html")


def system_logs(request):
    return render(request, "activity/store_logs.html")


def user_report(request):
    return render(request, "activity/incomereport.html")


def wallet_report(request):
    return render(request, "activity/admin_transaction.html")


def Graphs_report(request):
    return render(request, "activity/admin_statistics.html")


# wallet
def wallet_all_transactions(request):
    return render(request, "wallet/mywallet.html")


def withdraw_requests(request):
    return render(request, "wallet/wallet_requests_list.html")


def wallet_payment_gateway(request):
    return render(request, "wallet/withdrawal_payment_gateways.html")


def settings(request):
    return render(request, "wallet/wallet_setting.html")


# mlm
def mlm_settings(request):
    return render(request, "mlm/mlm_settings.html")


def mlm_levels(request):
    return render(request, "mlm/mlm_levels.html")


# saas
def sass_setting(request):
    return render(request, "saas/saas_setting.html")


def sass_transactions(request):
    return render(request, "saas/vendor_deposits.html")


# user
def user_list(request):
    return render(request, "users/userslist.html")


def user_groups(request):
    return render(request, "users/usergroup.html")


def user_referring_tree(request):
    return render(request, "users/userslisttree.html")


def user_mail_sender(request):
    return render(request, "users/userslistmail.html")


def user_manage_admin(request):
    return render(request, "users/admin_user.html")


# Membership
def membrership_plans(request):
    return render(request, "membership/plans.html")


def membrership_orders(request):
    return render(request, "membership/membership_orders.html")


def membrership_setting(request):
    return render(request, "membership/settings.html")


# local store
def store_dashboard(request):
    return render(request, "local store/store_dashboard.html")
