from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Tutorial, TutorialSeries, TutorialCategory
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import NewUserForm

#we need to handle the views for single slashes which point to other than anything we already have
def single_slash(request, single_slash):
    categories = [c.category_slug for c in TutorialCategory.objects.all()]
    if single_slash in categories:
        matching_series = TutorialSeries.objects.filter(tutorialcategory__category_slug=single_slash)
        
        series_urls ={}
        for m in matching_series.all():
            part_one = Tutorial.objects.filter(tutorialseries__series = m.series).earliest("tutorials_published")
            series_urls[m] = part_one.tutorials_slug
        
        return render(request=request,
                      template_name='main/category.html',
                      context={"tutorial_series": matching_series, "part_one": series_urls})

    tutorials = [t.tutorials_slug for t in Tutorial.objects.all()]
    if single_slash in tutorials:
        return HttpResponse(f"{single_slash} is a tutorial")


    return HttpResponse(f"{single_slash} does not correspond to anything")


def homepage(request) : 
    #return HttpResponse("This is the initial website")
    return render(request = request,
     template_name = "main/categories.html",
     context = {"categories" : TutorialCategory.objects.all})

#An already defined User creation form comes with Django, we can use it as it is like below or import it 
#and overrite it if we want to
def register(request):

    #following code will handle POST requests
    if request.method == 'POST':
        print("POST method initiated")
        form = NewUserForm(request.POST)
        if form.is_valid():
            print("valid")
            user = form.save()
            username = form.cleaned_data.get('username')
            #displays messages, inbuilt library in django
            messages.success(request,f"New Account Created : {username}")
            login(request,user)
            messages.info(request,f"You are now logged in as : {username}")

            return redirect("main:homepage")
        else:
            for msg in form.error_messages:
                messages.error(request,f"{msg} : {form.error_messages[msg]}")
  
    form  = NewUserForm
    return render(request = request,
     template_name = "main/register.html",
     context = {"form" : form})


def logout_request(request):
#logs user out, just have to create aurl, we dont need to create a template
    logout(request)
    messages.info(request,"You have successfully logged out ")
    return redirect("main:homepage")

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid() :
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username= username,password =password)
            if user is not None :
                login(request, user)
                messages.info(request,f"You are now logged in as : {username}")
            else:
                 messages.error(request,"Invalid username or password")
        else:
            messages.error(request,"Invalid username or password")


    form = AuthenticationForm
    return render(request = request,
     template_name = "main/login.html",
     context = {"form" : form})
