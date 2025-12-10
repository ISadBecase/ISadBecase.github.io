from django.shortcuts import render
def go_a(request):
    username=request.GET.get("username")
    age=request.GET.get("age")
    
    print("go_a")
    # render 函数常用参数：
    # request: 函数的形式参数request
    # template_name: 访问的页面，以template为起点
    # context: 返回给页面的数据，键值对格式，页面可以通过{{key}}取出对应的value
    # content_type: 如果需要返回数据给页面的时候，以什么格式返回
    return render(request, 'a.html', {'username': username, 'age': age})
def go_login(request):
    return render(request, 'login.html')