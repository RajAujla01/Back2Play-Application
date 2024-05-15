from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

from django.utils import timezone
from datetime import datetime, timedelta
from django.db import models
import datetime



class MyAccountManager(BaseUserManager): #custom user manager for user model. Extends BaseUserManager 
                                        #if using custom user manager must override the following 2 functions

    def create_user(self, email, username, password):           #for a new user. Email and username are both required 
        if not email:
            raise ValueError("You must have an email address!") #raise error if no email address 
        if not username:
            raise ValueError("You must have a username!")
        user = self.model(                                      #create the user with parameters specified 
            email=self.normalize_email(email),                  #convert email characters to lowercase 
            username=username, password=password)

        user.set_password(password)                             #set password for user 
        user.save(using=self._db)                               #saves user into database 
        return user                                             
    
    def create_superuser(self, email, username, password): #for a superuser 
        user = self.create_user(
            email=self.normalize_email(email), 
            username=username,
              password=password
        )
        user.is_active = True                   #These are all set to true as this user is a superuser with special access and permissions
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
 


class Account(AbstractBaseUser): #extends AbstractBaseUser class 
    email                   = models.EmailField(verbose_name="email", max_length=60, unique=True) #can only have one user with that email
    username                = models.CharField(max_length=30, unique=True)
    date_joined             = models.DateTimeField(verbose_name='date joined', auto_now_add=True) #automatically adds current datetime
    last_login              = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin                = models.BooleanField(default=False)     #all of these fields are required for a custom user model 
    is_active               = models.BooleanField(default=True)      #set to true as user is active 
    is_staff                = models.BooleanField(default=False)     #other defaults set to false as user is regular user 
    is_superuser            = models.BooleanField(default=False)      
    
    USERNAME_FIELD = 'email'    #what we want the user to log in with 
    REQUIRED_FIELDS = ['username'] #required field for registration other than username 

    objects = MyAccountManager()            #references account manager above 

    def __str__(self):
        return self.email + ", " + self.username #what will display when an account object is printed to a template 
    
    def has_perm(self, perm, obj=None):         #required functions for custom user 
        return self.is_admin                    #check if user has permissions, check if user is admin  
    
    def has_module_perms(self, app_label):      #check if user has access to modules 
        return True
    
    

    

class Profile(models.Model):
    user = models.OneToOneField(Account, null=True, on_delete=models.CASCADE) #one to one associated with Account model

    position = models.IntegerField(default=1)                                  #default set to one so user initialised 

    def __str__(self):
        return str(self.user)
    



class MemberLastCompleteHistory(models.Model):
    user = models.OneToOneField(Account, null=True, on_delete=models.CASCADE) #delete objects that have relationship with this object 

    session_complete_1 = models.DateTimeField(null=True, default=None)  #set null to True so values are empty until sessions are completed 
    
    session_complete_2 = models.DateTimeField(null=True, default=None)

    session_complete_3 = models.DateTimeField(null=True, default=None)

    session_complete_4 = models.DateTimeField(null=True, default=None)

    session_complete_5 = models.DateTimeField(null=True, default=None)

    session_complete_6 = models.DateTimeField(null=True, default=None)

    session_complete_7 = models.DateTimeField(null=True, default=None)

    session_complete_8 = models.DateTimeField(null=True, default=None)

    session_complete_9 = models.DateTimeField(null=True, default=None)

    session_complete_10 = models.DateTimeField(null=True, default=None)

    session_complete_11 = models.DateTimeField(null=True, default=None)

    session_complete_12 = models.DateTimeField(null=True, default=None)
    

    def __str__(self):
        return str(self.user)


