from django import forms
#new test


class VideoForm(forms.Form):
 
    uservidchoice = forms.CharField(max_length=200)



