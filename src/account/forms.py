from django import forms
from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth import authenticate
from account.models import Account, Profile #import our created models 


class RegistrationForm(UserCreationForm): #extends UserCreationForm 
    email = forms.EmailField(max_length=60, help_text='This field is required. Please add a valid email address.') #our custom field 

    class Meta:                                 #tell form additional information              
        model = Account                         #references Account model 
        fields = ("email", "username", "password1", "password2")    #2 passwords for confirmation 



class AccountAuthenticationForm(forms.ModelForm): #form based on Account model, tells which fields to use 
    password = forms.CharField(label='Password', widget=forms.PasswordInput) #hides password when user is entering it  

    class Meta:
        model = Account
        fields = ('email', 'password')          #visible fields 

    def clean(self):                            #before form does anything it runs logic from this function 
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                raise forms.ValidationError("Invalid login!")       #if credentials not valid display this error 
        


class AccountUpdateForm(forms.ModelForm):

    class Meta:
        model = Account
        fields = ('email', 'username')

    def clean_email(self):
            email = self.cleaned_data['email']
            try:
                account = Account.objects.exclude(pk=self.instance.pk).get(email=email) #check if account exists 
            except Account.DoesNotExist: #otherwise 
                return email
            raise forms.ValidationError("This email is already in use, please choose a different one.")

    def clean_username(self):
            username = self.cleaned_data['username']
            try:
                account = Account.objects.exclude(pk=self.instance.pk).get(username=username) #check if username already in use
                                                                                            #get primary key, can query account if exists 
            except Account.DoesNotExist:
                return username
            raise forms.ValidationError("This username is already in use, please choose a different one.")

       

class WorkoutCompletedForm(forms.Form):
    pass


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user', 'position']  # Include fields you want to display in the form

