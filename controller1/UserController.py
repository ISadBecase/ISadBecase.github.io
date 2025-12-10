from django.shortcuts import render
from django.http import JsonResponse
from Service import UserService as us
def login(request):
    print("验证成功")
    username = request.GET.get('username')
    password = request.GET.get('password')
    print("用户名：", username)
    print("密码", password)
    return JsonResponse(us.login(username, password))