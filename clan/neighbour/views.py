from django.shortcuts import render
from .forms import UserProfileForm,NeighborhoodForm,BusinessForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,authenticate
from .models import UserProfile,Neighborhood,Business,Service
from django.http import Http404
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

def index(request):
    neighborhood = Neighborhood.objects.all()
    return render(request,'index.html',{"neighborhood":Neighborhood})

def neighborhood(request):
    '''
    function to fill the neighborhood form
    '''
    current_user = request.user
    try:
        if request.method == 'POST':
            form = NeighborhoodForm(request.POST,request.FILES)
            if form.is_valid():
                neighborhood = form.save(commit = False)
                neighborhood.user = current_user
                neighborhood.save()
            return redirect('/profile')
        else:
            form = NeighborhoodForm()

    except ValueError:
        Http404
    return render(request,'neighborhood.html',{"form":form,})
