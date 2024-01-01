from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render,redirect
from django.db.models.signals import post_save
from decorators import unauthenticated_user, allowed_users
from .models import *
from .forms import ListingForm, CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .filters import ListingFilter
from .forms import CommentForm



def aboutpage(request):
    return render(request, 'index.html')


def favourite_list(request):
    
    user = request.user
    favourite_posts = Listing.objects.filter(favourites=user)
    return render(request, 'favourite_list.html', {
        'favourite_posts':favourite_posts,
    })



def favourite(request,id):
    listing = get_object_or_404(Listing, id=id)
    if listing.favourites.filter(id=request.user.id).exists():
       listing.favourites.remove(request.user)
    else:
        listing.favourites.add(request.user)
    return HttpResponseRedirect(listing.get_absolute_url())  



def frontpage(request):
    posts = Post.objects.all()
    return render(request, 'frontpage.html', {'posts': posts})

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.name = request.user
            comment.email = request.user
            comment.save()

            return redirect('post_detail', slug=post.slug)
    else:
        form = CommentForm()

    return render(request, 'post_detail.html', {'post': post, 'form': form})


@login_required(login_url='login')
def register_page(request):

    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect("login")
        messages.error(request, 'Invalid')
    
    return render(request, "signup.html",{
        "form":form
    })

@unauthenticated_user
def login_page(request):
    
    if request.method == "POST":
        username= request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/') 
        else:
            messages.info(request, 'Username or Password is incorrect')    
        
    return render(request, "login2.html")

@login_required(login_url='login')
def logout_user(request):
    logout(request)
    return redirect('/')

#CRUD- Create Retrieve Update Delete (List) for database ad listings
def index(request):
    listings = Listing.objects.all() #[:3] for 3 results

    myFilter = ListingFilter(request.GET, queryset=listings)
    listing = myFilter.qs

    return render(request, "index2.html",{
         "listings": listings,
         "myFilter": myFilter,
         "listing": listing
    })

def listing_retrieve(request, pk):
    listing = Listing.objects.get(id=pk)
    is_favourite = False
    if listing.favourites.filter(id=request.user.id).exists():
        is_favourite = True

    return render(request, "listing.html",{
        "listing":listing,
        "is_favourite":is_favourite,
    })

@login_required(login_url='login')
#@allowed_users(allowed_roles=['admin'])
def listing_create(request):
    form = ListingForm()

    if request.method == "POST":
        form=ListingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/")
    
    return render(request, "listing_add.html",{
        "form":form
    })

@login_required(login_url='login')
#@allowed_users(allowed_roles=['admin'])
def listing_update(request, pk):
    
    listing = Listing.objects.get(id=pk)
    form = ListingForm(instance=listing)

    if request.method == "POST":
        form=ListingForm(request.POST, instance=listing, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/")

    return render(request, "listing_update.html",{
        "form":form
    })

def listing_delete(request,pk):
    listing=Listing.objects.get(id=pk)
    listing.delete()
    return redirect("/")
   