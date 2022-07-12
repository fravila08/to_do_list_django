
from re import T
from urllib import response
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
import json
from django.views.decorators.csrf import csrf_exempt
from .models import AppUser as User, To_do


# clean=To_do.objects.create(activity='clean')
# payBills=To_do.objects.create(activity='pay bills')
# oilchange=To_do.objects.create(activity='change oil')





@csrf_exempt
def home(request):
    if request.method=='GET':
        items=To_do.objects.all()
        user=request.user.email 
        context={
            'email': user,
            'items':items
            }
        return render(request, 'to_do_app/home.html', context)
    if request.method=='POST':
        try:
            body=json.loads(request.body)
            item=To_do.objects.get(id= body['item'])
            print(item)
            item.delete()
            return JsonResponse({'success':True})
        except Exception as e:
            return JsonResponse({'success':False})



@csrf_exempt
def signup(request):
    if request.method=='GET':
        return render(request, 'to_do_app/signup.html')
    if request.method=='POST': 
        try:
            body= json.loads(request.body)
            User.objects.create_user(username=body['email'], email=body['email'], password=body['password'])
            return JsonResponse({'success':True})
        except Exception as e:
            print('oops')
            print(str(e))
            return JsonResponse({'success':False})








@csrf_exempt
def signin(request):
    if request.method=='GET':
        return render(request, 'to_do_app/signin.html')
    if request.method=='POST':
        body=json.loads(request.body)
        email=body['email']
        password=body['password']
        user=authenticate(username=email, password=password)
        if user is not None:
            if user.is_active:
                try:
                    login(request, user)
                    return JsonResponse({'Success':True})
                except Exception as e:
                    return JsonResponse({'Success': False, 'reason':'login failed'})
            else:
                return JsonResponse({'Success': False, 'reason':'disabled'})
        else:
            return JsonResponse({'Success': False, 'reason':'does not exist'})
    
    
    