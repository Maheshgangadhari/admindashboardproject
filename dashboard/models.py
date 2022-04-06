
# # ==========users=============
#
# # class userslist(models.Model):
# #     firstname
# #     lastname
# #     mobile
# #     email
#     usermembershipplan
#     vendorstaus--disable Eanble
#     username
#     password
#     repeatpassword
#     underaffilite---user list
#     underlevel----level1,level2,level3
#     country---countries list
#     groups
# # #
# # class usergroup(models.Model):
# #     sn--id
# #     image
# #     groupname
# #     numberofusers
# #     numberofcampaigns
# #     description
# #     isdefalut
# #
# # class adminuser(models.Model):
# #     firstname
# #     lastname
# #     email
# #     username
# #     phonenumber
# #     country
# #     city
# #     pincode
# #     password
# #     repassword
# #     memberimage
#
# # =============membership===================
# # class MembershipPlans(models.Model):
# #     Name
# #     PlanUserType
# #     Price
# #     Bonus
# #     CommissionSaleStatus
# #     BillingPeriod
# #     Usertype
# #     labeltext
# #     labelbackground
# #     labelcolor
# #     description
# #     sortorder
# #     display
# #     planicon
# #
# # class MemberOrders(models.Model):
# #     username
# #     planname
# #     price
# #     ordertype
# #     isactive
# #     planstatus
# #     paymentmethod
# #     remaningtime
# #     startdate
# #     enddate
# #     Createdat
#
# #
# # class MembershipSettings(models.Model):
# #     status
# #     Showexpirenotificationinterval
# #     Defaultplanfornewregistermember
