from django.contrib import admin
from django.contrib.auth.admin import UserAdmin #for making admin screens 
from account.models import Account, Profile, MemberLastCompleteHistory


class AccountAdmin(UserAdmin): #custom class that extends UserAdmin class
    list_display = ('email', 'username', 'date_joined', 'last_login', 'is_admin', 'is_staff') #columns we want to see 
    search_fields = ('email', 'username',)                                              #fields we can search, creates search bar 
    readonly_fields = ('date_joined', 'last_login')                                     #can't be edited 

    filter_horizontal = ()                                  #left to default 
    list_filter     = ()                                    #allows for filtering with argument 
    fieldsets       = ()                                    

admin.site.register(Account, AccountAdmin)                  #register model to admin site to see in Django admin page  
admin.site.register(Profile)
admin.site.register(MemberLastCompleteHistory)