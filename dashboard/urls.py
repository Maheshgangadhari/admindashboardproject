from dashboard.views import dashboard, addons, affliate_theme, award, currency_list, language, paymentset, \
    system_status, all_transactions, payment_gateway, category, system_orders, compaigns, programs, system_logs, \
    user_report, wallet_report, settings, sass_setting, mlm_levels, mlm_settings, sass_transactions, user_list, \
    user_groups, user_referring_tree, user_mail_sender, user_manage_admin, membrership_orders, membrership_setting, \
    store_dashboard, withdraw_requests, membrership_plans, Graphs_report, wallet_all_transactions, \
    wallet_payment_gateway
from django.urls import path

urlpatterns = [
    path('', dashboard, name='dashboard'),

    # profile
    # path('profile/',Profile,name='profile'),
    # usefull links
    path('add/', addons, name='addons'),
    path('themes/', affliate_theme, name='aff'),
    path('award level/', award, name='award'),
    path('currency/', currency_list, name='currency_list'),
    path('language/', language, name='language'),
    path('system_status/', system_status, name='system_status'),
    path('payset/', paymentset, name='paymentsetss'),

    path('all_transactions/', all_transactions, name='all_transactions'),
    path('payment_gateway/', payment_gateway, name='payment_gateway'),

    # marketing
    path('compaigns/', compaigns, name='campaigns'),
    path('programs/', programs, name='programs'),
    path('category/', category, name='category'),

    # activity
    path('system_orders/', system_orders, name='system_orders'),
    path('system_logs/', system_logs, name='system_logs'),
    path('user_report/', user_report, name='user_report'),
    path('wallet_report/', wallet_report, name='wallet_report'),
    path('Graphs_report/', Graphs_report, name='Graphs_report'),

    # wallet
    path('wallet_all_trans/', wallet_all_transactions, name='wallet_all_trans'),
    path('withdraw_requests/', withdraw_requests, name='withdraw_requests'),
    path('wallet_pay/', wallet_payment_gateway, name='wallet_payment_gate'),
    path('setting/', settings, name='setting'),
    # mlm
    path('mlm_settings/', mlm_settings, name='mlm_settings'),
    path('mlm_levels/', mlm_levels, name='mlm_levels'),

    path('sass_setting/', sass_setting, name='sass_setting'),
    path('sass_transactions/', sass_transactions, name='sass_transactions'),

    path('user_list/', user_list, name='user_list'),
    path('user_groups/', user_groups, name='user_groups'),
    path('user_referring_tree/', user_referring_tree, name='user_referring_tree'),
    path('user_mail_sender/', user_mail_sender, name='user_mail_sender'),
    path('user_manage_admin/', user_manage_admin, name='user_manage_admin'),

    path('membrership_plans/', membrership_plans, name='membrership_plans'),
    path('membrership_orders/', membrership_orders, name='membrership_orders'),
    path('membrership_setting/', membrership_setting, name='membrership_setting'),

    path('store_dashboard/', store_dashboard, name='store_dashboard'),

]
