from django import forms
from django.contrib.auth.forms import UserCreationForm

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['user','name','avatar','neighbourhood','location']
class NeighborhoodForm(forms.ModelForm):
    class Meta:
        model = Neighborhood
        fields = ['name','locaion','occupant_count']
#class PostForm(forms.ModelForm):
    #class Meta:
        #model = Post
        #fields = ['title','post','profile','user']
class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ['name','user','neighborhood','email']
