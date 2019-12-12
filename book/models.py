from django.db import models
from django import forms

#用户信息表
class Users(models.Model):
    u_id = models.CharField(max_length=10, unique = True)
    u_password = models.CharField(max_length=255)

    class Meta:
        db_table = 'Users'

#登录表单
class UserForm(forms.Form):
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

#注册表单
class RegisterForm(forms.Form):
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="确认密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

#书目类别
class Category(models.Model):
    id = models.IntegerField('id',primary_key=True)
    name = models.CharField('name',max_length=40)
    disable = models.BooleanField('disable')

    class Meta:
        db_table = 'category'

#可借数量
class BookStatus(models.Model):
    isbn = models.CharField('isbn', primary_key=True, max_length=13, unique=True)
    book_number = models.IntegerField('book_number', default=0)
    lend_number = models.IntegerField('lend_number', default=0)

    class Meta:
        db_table = 'book_status'

#图书信息
class BookInfo(models.Model):
    isbn = models.CharField('isbn',primary_key=True, max_length=13,unique = True)
    bookName = models.CharField('bookName', max_length=100)
    author = models.CharField('author',max_length=100)
    press = models.CharField('press',max_length=100)
    category_id = models.IntegerField('category_id',default=0)
    book_number = models.IntegerField('book_number',default=0)

    class Meta:
        db_table = 'book_info'