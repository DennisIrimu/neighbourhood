from django.shortcuts import render
from .forms import UserProfileForm,NeighborhoodForm,BusinessForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,authenticate
from .models import UserProfile,Neighborhood,Business,Service
from django.http import Http404
# Create your views here.

@login_required(login_url='/accounts/login/')
def update_profile(request):
    '''
    function to update the profile form
    '''
    title="Neighborhood | Profile Edit "
    current_user = request.user
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user=current_user
            if UserProfile.objects.filter(user_id=current_user.id).exists():
                UserProfile.objects.filter(user_id=current_user.id).delete()
            profile.save()
            return redirect('/')

    else:
        form = UserProfileForm()

    return render(request, 'editprofile.html', {"title":title,"form": form})
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

def business(request):
    '''
    function to create a new business
    '''
    current_user = request.user
    try:
        if request.method == 'POST':
            form = BusinessForm(request.POST,request.FILES)
            if form.is_valid():
                post = form.save(commit = False)
                post.user = current_user
                post.save()
            return redirect('/viewbusiness')
        else:
            form = BusinessForm()

    except ValueError:
        Http404
    return render(request,'business.html',{"form":form,})

def viewBusiness(request):
    '''
    function to view business
    '''
    business = Business.objects.all()
    return render(request,'viewbusiness.html',{"business":business})

def post(request):
    '''
    function to create a new post
    '''
    current_user = request.user
    try:
        if request.method == 'POST':
            form = PostForm(request.POST,request.FILES)
            if form.is_valid():
                post = form.save(commit = False)
                post.user = current_user
                post.save()
            return redirect('/viewpost')
        else:
            form = PostForm()

    except ValueError:
        Http404
    return render(request,'post.html',{"form":form,})

def viewPost(request):
    '''
    function to view posts
    '''
    posts= Post.objects.all()
    return render(request,'viewpost.html',{"posts":posts})
