from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Count
from django.contrib import auth 
from .models import Questionary
from django.db import connection


# Create your views here.
def index(request):
	if request.user.is_authenticated:
		username = auth.get_user(request).username
		return render(request, 'profile_user/index.html',
			context={'username':username}
		)
	else:
		return redirect('/main/')

 
# сохранение данных в бд
def create_data(request):
    if request.user.is_authenticated:
        username = auth.get_user(request).username
    if request.method == "POST":
        row = ""
        age = request.POST.get("age")
        fname = request.POST.get("firstname")
        lname = request.POST.get("lastname")
        act = request.POST.get("activity")
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM profile_user_Questionary q WHERE q.age = {age} AND q.first_name = '{fname}' AND q.last_name = '{lname}' AND q.activity = '{act}'")
        row = cursor.fetchall()
        if len(row) == 0:
            data_user = Questionary()
            data_user.age = age
            data_user.first_name = fname
            data_user.last_name = lname
            data_user.activity = act
            data_user.email = request.POST.get("email")
            data_user.link = request.POST.get("link")
            data_user.save()
            return HttpResponseRedirect('/products/')
        else:
            user_exists = " user exists, try again or exit"
            return render(request, 'profile_user/index.html', {'username':username, 'user_exists':user_exists}, )
         
