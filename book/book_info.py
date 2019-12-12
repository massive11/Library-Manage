from django.http import HttpResponse
from .models import BookInfo
from . import models
from .models import BookStatus
from django.shortcuts import render
from django.forms.models import model_to_dict
import json
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render,redirect

# 添加页面的数据交互
def add(request):
    request.encoding = 'utf-8'
    #ctx = {}
    if request.POST:
        isbn = request.POST['input-isbn']
        bookName = request.POST['input-name']
        author = request.POST['input-author']
        press = request.POST['input-press']
        #category_id = request.POST['input-category']
        category_id = request.POST.get("selectCategory")
        book_number = request.POST['input-num']
        available = request.POST['input-num']
        print(isbn, bookName, author, press, category_id, book_number)
        book = BookInfo(isbn=isbn, bookName=bookName, author=author, press=press, category_id=category_id,
                        book_number=book_number)
        status = BookStatus(isbn = isbn, book_number=book_number,lend_number=available)
        status.save()
        book.save()
    return render(request, "add.html")

#查询页面的数据展示
@csrf_exempt
def bookInfo(request):
    if not request.session.get('is_login', None):
        #     登录状态不允许注册。你可以修改这条原则！
            return redirect("/book/index")
    request.encoding = 'utf-8'
    books = []
    if True:
        book = BookInfo.objects.all()
        for e in book:
            eDirt = model_to_dict(e)
            sta = BookStatus.objects.filter(isbn=eDirt['isbn']).values('lend_number').first()
            eDirt['lend_number'] = sta['lend_number']
            books.append(eDirt)

    print(books)
    return render(request, "bookInfo.html", {'books_ret': books})

#查询页面的输入框搜索
@csrf_exempt
def bookSearch(request):
    request.encoding = 'utf-8'
    arr = []
    if request.POST:
        s_name = request.POST.get("search-name")
        s_isbn = request.POST.get("search-isbn")
        s_id = request.POST.get("s_category")
        print(s_id)
        if s_id == '0':
            search_result = BookInfo.objects.filter(bookName__contains=s_name, isbn__contains=s_isbn)
        else:
            search_result = BookInfo.objects.filter(category_id = s_id, bookName__contains=s_name, isbn__contains=s_isbn)
        for i in search_result:
            iDirt = model_to_dict(i)
            st = BookStatus.objects.filter(isbn=iDirt['isbn']).values('lend_number').first()
            iDirt['lend_number'] = st['lend_number']
            arr.append(iDirt)
    print(arr)
    return HttpResponse(json.dumps(arr), content_type='application/json')


# 删除图书时的数据库交互
@csrf_exempt
def delete(request):
    r = request.POST.get("isbn")
    models.BookInfo.objects.filter(isbn=r).delete()
    models.BookStatus.objects.filter(isbn = r).delete()
    return HttpResponse(json.dumps({}), content_type='application/json')

# 根据类别id获取类别
@csrf_exempt
def getCategory(request):
    request.encoding = 'utf-8'
    rets=[]
    if request.POST:
        t = request.POST.get("title")
        search_id = models.Category.objects.filter(name = t).values('id')
        search_r = models.BookInfo.objects.filter(id = search_id['id'])
        for i in search_r:
                rets.append(model_to_dict(i))
    print(rets)
    return HttpResponse(json.dumps(rets), content_type='application/json')


#修改页面的数据交互
@csrf_exempt
def update(request):
    request.encoding = 'utf-8'
    r = request.POST.get("isbn")
    name = request.POST.get("book-name")
    b_author = request.POST.get("book-author")
    b_press = request.POST.get("book-press")
    n_category = request.POST.get("book-category")
    number = request.POST.get("book-number")
    a_number = request.POST.get("book-available")
    models.BookInfo.objects.filter(isbn = r).update(bookName = name, author = b_author, press = b_press, category_id = n_category, book_number = number)
    models.BookStatus.objects.filter(isbn = r).update(book_number = number, lend_number = a_number)
    print(r,name,b_author,b_press,n_category,number,a_number)
    return HttpResponse(json.dumps({}), content_type='application/json')