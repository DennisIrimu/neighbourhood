from django.shortcuts import render
from .forms import UserProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,authenticate
# Create your views here.

@login_required(login_url='/accounts/login/')
def profile(request,id):
    '''
    function to display the user profile
    '''
    current_user = request.user
    current_user.id = request.user.id
    current_profile = UserProfile.objects.get(user_id = current_user.id)
    try:
        profile = UserProfile.objects.get(user_id = current_user.id)


        return render(request, 'profile.html', {"profile":profile,"id":current_user.id})


    except ValueError:
        raise Http404()
