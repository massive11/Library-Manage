from django.shortcuts import render,redirect
from . import models
from .models import UserForm
from .models import RegisterForm
import hashlib

def index(request):
    pass
    return render(request,'index.html')

def login(request):
    if request.session.get('is_login', None):
       return redirect("/book/info")
    if request.method == "POST":
        login_form = UserForm(request.POST)
        message = "请检查填写的内容！"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            print(username,password)
            try:
                user = models.Users.objects.get(u_id=username)
                if user.u_password == hash_code(password):  # 哈希值和数据库内的值进行比对
                    request.session['is_login'] = True
                    request.session['user_id'] = user.u_id
                    request.session['user_name'] = user.u_password
                    return redirect('/book/info')
                else:
                    message = "密码不正确！"
            except:
                message = "用户不存在！"
        return render(request, 'login.html', locals())

    login_form = UserForm()
    return render(request, 'login.html', locals())

def register(request):
    if request.session.get('is_login', None):
        # 登录状态不允许注册。你可以修改这条原则！
        return redirect("/book/info")
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():  # 获取数据
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            if password1 != password2:  # 判断两次密码是否相同
                message = "两次输入的密码不同！"
                return render(request, 'register.html', locals())
            else:
                same_name_user = models.Users.objects.filter(u_id=username)
                if same_name_user:  # 用户名唯一
                    message = '用户已经存在，请重新选择用户名！'
                    return render(request, 'register.html', locals())
                # 当一切都OK的情况下，创建新用户

                new_user = models.Users.objects.create()
                new_user.u_id = username
                new_user.u_password = hash_code(password1)  # 使用加密密码
                new_user.save()
                return redirect('/book/login')  # 自动跳转到登录页面
    register_form = RegisterForm()
    return render(request, 'register.html', locals())

def logout(request):
    if not request.session.get('is_login',None):
        return redirect('/book/index')
    request.session.flush()

    return redirect('/book/index')

#哈希
def hash_code(s, salt='mysite'):
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())  # update方法只接收bytes类型
    return h.hexdigest()