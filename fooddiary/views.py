from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.http import HttpRequest
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import MealForm, ActivityForm
from .models import Meal, Activity
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'fooddiary/home.html')


def signupuser(request):
    if request.method == 'GET':
        return render(request, 'fooddiary/signupuser.html', {'form':UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('currentmeal')
            except IntegrityError:
                return render(request, 'fooddiary/signupuser.html', {'form':UserCreationForm() , 'error':'That username is alredy taken. Please try another one.'})    
        else:
            return render(request, 'fooddiary/signupuser.html', {'form':UserCreationForm() , 'error':'Passwords did not match. Please try again.'})

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'fooddiary/login.html', {'form':AuthenticationForm()})
    else:
        user = authenticate(request,username =request.POST['username'] , password=request.POST['password'] )
        if user is None:
            return render(request, 'fooddiary/login.html', {'form':AuthenticationForm(), 'error':'Username and passsword did not match'})    
        else:
            login(request, user)
            return redirect('currentmeal')

@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

@login_required
def currentmeal (request):
    meal = Meal.objects.filter(user = request.user).order_by('-date')
    return render(request, 'fooddiary/currenttodos.html', {'meals':meal} )

@login_required
def createmeal(request):
    if request.method == 'GET':
        return render(request, 'fooddiary/createmeal.html', {'form':MealForm()})
    else:
        try:
            form = MealForm(request.POST)
            newMeal = form.save(commit=False)
            newMeal.user = request.user
            newMeal.save()
            return redirect('currentmeal')
        except ValueError:
            return render(request, 'fooddiary/createmeal.html', {'form':MealForm(), 'error':'Your meal couldn\'t register. Please try another title or description.'})

@login_required
def viewmeal (request, meal_pk):
    meal = get_object_or_404(Meal, pk = meal_pk, user = request.user)
    
    if request.method == 'GET':
        form = MealForm(instance=meal)
        print (meal)
        return render(request, 'fooddiary/viewmea1l.html', {'meal':meal,'id':meal_pk, 'form':form} )
    else:
        try:
            print(meal)
            form = MealForm(request.POST, instance=meal)
            form.save()
            return redirect('currentmeal')

        except ValueError:
            return render(request, 'fooddiary/viewmea1l.html', {'meal':meal,'id':meal_pk, 'form':form, 'error':'Your meal couldn\'t register. Please try another title or description.'})

@login_required
def deletemeal(request, meal_pk):
    meal = get_object_or_404(Meal, pk = meal_pk, user = request.user)
    if request.method == 'POST':
        meal.delete()
        return redirect('currentmeal')

def physicalactivity(request):
    activity = Activity.objects.filter(user = request.user).order_by('-date')
    return render(request, 'fooddiary/physicalactivity.html', {'activities':activity} )  

def createactivity(request):
    if request.method == 'GET':
        return render(request, 'fooddiary/createactivity.html', {'form':ActivityForm()})
    else:
        try:
            form = ActivityForm(request.POST)
            newActivity = form.save(commit=False)
            newActivity.user = request.user
            newActivity.save()
            return redirect('physicalactivity')
        except ValueError:
            return render(request, 'fooddiary/createactivity.html', {'form':ActivityForm(), 'error':'Your activity couldn\'t register. Please try another title or description.'})

def viewactivity (request, activity_pk):
    activity = get_object_or_404(Activity, pk = activity_pk, user = request.user)
    
    if request.method == 'GET':
        form = ActivityForm(instance=activity)
        return render(request, 'fooddiary/viewactivity.html', {'activity':activity,'id':activity_pk, 'form':form} )
    else:
        try:
            form = ActivityForm(request.POST, instance=activity)
            form.save()
            return redirect('physicalactivity')
        except ValueError:
            return render(request, 'fooddiary/viewactivity.html', {'activity':activity,'id':activity_pk, 'form':form, 'error':'Your meal couldn\'t register. Please try another title or description.'})

def deleteactivity(request, activity_pk):
    activity = get_object_or_404(Activity, pk = activity_pk, user = request.user)
    if request.method == 'POST':
        activity.delete()
        return redirect('physicalactivity')

def weekmeal(request):
    meal = Meal.objects.filter(user = request.user).order_by('-date')[:7]
    activity = Activity.objects.filter(user = request.user).order_by('-date')[:7]
    return render(request, 'fooddiary/weeklysummary.html', {'meals':meal,'activities':activity} )

def favourite(request):
    meal = Meal.objects.filter(user = request.user, favourite = True).order_by('-date')
    return render(request, 'fooddiary/favourite.html', {'meals':meal})