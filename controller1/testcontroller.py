from django.shortcuts import render
from django.http import JsonResponse
def re_json(request):
    dict_data={"name":"张三","age":18}
    return JsonResponse(dict_data)