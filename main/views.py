from django.shortcuts import render, redirect
from django.utils import *
from .models import Goal

def main_login(request):
    return render(request, 'main/main_login.html')


def main_logout(request):
    return render(request, 'main/main_logout.html')


def goal_main(request):
    goals = Goal.objects.all()
    return render(request, 'main/goal_main.html', {'goals':goals})


def add_goal(request):
    return render(request, 'main/add_goal.html')

def create_goal(request):
    new_goal = Goal()
    new_goal.category = request.POST['category']
    new_goal.certify_method = request.POST['certify_method']
    new_goal.manager = request.user
    new_goal.name = request.POST['name']
    new_goal.description = request.POST['description']
    new_goal.created = timezone.now()
    new_goal.start_date = request.POST['start_date']
    new_goal.fee = request.POST['fee']
    new_goal.criteria = False

    # 인증 방식이 수치인 경우 인증 기준의 값과 단위를 db에 저장
    if request.POST['certify_method'] == 'figure':
        new_goal.criteria = True
        new_goal.value = request.POST['value']
        new_goal.unit = request.POST['unit']
    
    new_goal.save()    
    return redirect('main:goal_main')