from django.db import models

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

