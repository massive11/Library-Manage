# Generated by Django 2.2.7 on 2019-12-08 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookStatus',
            fields=[
                ('isbn', models.CharField(max_length=8, primary_key=True, serialize=False, unique=True, verbose_name='isbn')),
                ('book_number', models.IntegerField(default=0, verbose_name='book_number')),
                ('lend_number', models.IntegerField(default=0, verbose_name='lend_number')),
            ],
            options={
                'db_table': 'book_status',
            },
        ),
        migrations.RemoveField(
            model_name='bookinfo',
            name='lend_number',
        ),
    ]
