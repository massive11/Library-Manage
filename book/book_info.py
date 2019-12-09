from django.http import HttpResponse
from .models import BookInfo
from . import models
from .models import BookStatus
from django.shortcuts import render
from django.forms.models import model_to_dict
import json
from django.views.decorators.csrf import csrf_exempt


# 添加页面的数据交互
def add(request):
    request.encoding = 'utf-8'
    ctx = {}
    if request.POST:
        isbn = request.POST['input-isbn']
        bookName = request.POST['input-name']
        author = request.POST['input-author']
        press = request.POST['input-press']
        category_id = int(request.POST['input-category'])
        book_number = int(request.POST['input-num'])

        print(isbn, bookName, author, press, category_id, book_number)
        book = BookInfo(isbn=isbn, bookName=bookName, author=author, press=press, category_id=category_id,
                        book_number=book_number)
        book.save()

    return render(request, "add.html")


#查询页面的数据展示
@csrf_exempt
def bookInfo(request):
    request.encoding = 'utf-8'
    books = []
    if request.POST:
        book = BookInfo.objects.all()
        for e in book:
            books.append(model_to_dict(e))
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
        search_result = BookInfo.objects.filter(bookName__contains=s_name, isbn__contains=s_isbn)
        for i in search_result:
            arr.append(model_to_dict(i))
        print(arr)
    return HttpResponse(json.dumps(arr), content_type='application/json')


# 删除图书时的数据库交互
@csrf_exempt
def delete(request):
    r = request.POST.get("isbn")
    models.BookInfo.objects.filter(isbn=r).delete()
    return HttpResponse(json.dumps({}), content_type='application/json')


# 根据类别id获取类别
@csrf_exempt
def getCategory(request):
    categories = models.Category.objects.filter(disable=0).all()
    rets = []
    for category in categories:
        rets.append({
            "id": category.id,
            "name": category.name
        })
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