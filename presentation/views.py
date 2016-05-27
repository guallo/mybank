import requests

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.


@login_required(login_url='login-view')
def dashboard_view(request):
    return render(request, 'presentation/dashboard.html')


@login_required(login_url='login-view')
def profile_view(request):
    return render(request, 'presentation/profile.html')


@login_required(login_url='login-view')
def accounts_view(request):
    result = requests.get('http://127.0.0.1:8000/core/accounts/', cookies=request.COOKIES)
    accounts = result.json()
    
    return render(request, 'presentation/accounts.html', {'accounts': accounts})


@login_required(login_url='login-view')
def saving_boxes_view(request):
    result = requests.get('http://127.0.0.1:8000/core/saving_boxes/', cookies=request.COOKIES)
    saving_boxes = result.json()
    
    return render(request, 'presentation/saving_boxes.html', {'saving_boxes': saving_boxes})


@login_required(login_url='login-view')
def moves_view(request):
    result = requests.get('http://127.0.0.1:8000/core/accounts/', cookies=request.COOKIES)
    accounts = result.json()
    result = requests.get('http://127.0.0.1:8000/core/saving_boxes/', cookies=request.COOKIES)
    saving_boxes = result.json()
    result = requests.get('http://127.0.0.1:8000/core/moves/', cookies=request.COOKIES)
    moves = result.json()
    
    return render(request, 'presentation/moves.html', {'accounts': accounts, 'saving_boxes': saving_boxes, 'moves': moves})