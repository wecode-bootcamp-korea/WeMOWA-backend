import os
import django
import csv
import  sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE','wemowa_main.settings')
django.setup()

from product.models import  Category, Product, StockStatus

CSV_PATH_PRODUCT = '../chromedriver/phonecases.csv'

with open(CSV_PATH_PRODUCT) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader,None)
    for row in data_reader:
        if row:
            stock = row[3]
           # StockStatus.objects.create(name = stock)
            collection = row[0]
            name = row[1]
            price = int(row[2].split(',')[0])
            description = row[4]
            category_id = Category.objects.get(name = row[0]).id
            stock_status_id = StockStatus.objects.get(name = stock).id
            print(category_id)
            Product.objects.create(category_id = category_id,collection=collection, name = name, price = price,stock_status_id = stock_status_id,description = description)
