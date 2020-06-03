import os
import django
import csv
import  sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE','wemowa_main.settings')
django.setup()

from product.models import  *

CSV_PATH_PRODUCT = '../chromedriver/output.csv'


with open(CSV_PATH_PRODUCT) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader,None)
#   악세사리 데이터 
#    for row in data_reader:
#        if row:
#            stock = row[3]
#            collection = row[0]
#            name = row[1]
#            price = int(row[2].split(',')[0])
#            description = row[4]
#            category_id = Category.objects.get(name = row[0]).id
#            collection_id = Collection.objects.get(name = row[0]).id
#            stock_status_id = StockStatus.objects.get(name = stock).id
#            # Product.objects.create(category_id = category_id,collection_id = collection_id, name = name, price = price,stock_status_id = stock_status_id,description = description)
#            image = row[5][2:len(row[5])-2]
#            images=image.split("', '")
#            product_id = Product.objects.get(name = row[1]).id
#            for img in images:
#                Image.objects.create(img_url = img, product_id = product_id)

    for row in data_reader:
        if row:
            collection = row[0]
            name = row[1]
            price = int(row[2].split(',')[0].replace('.',""))
            stock = row[3]
            stock_status_id = StockStatus.objects.get(name = stock).id
            description = row[4]
            category_id = Category.objects.get(id=1).id
            collection_id = Collection.objects.get(name = row[0]).id
            detail = row[9]
            image_string = row[5][2:len(row[5])-2]
            images = image_string.split("', '")
            luggage_color =row[6]
           # color_url_string = row[7][1:len(row[7])-1]
           # color_urls = color_url_string.split(', ')
            color_urls = row[7]
            color_url_eval = eval(color_urls)
            a=color_url_eval[row[6]]
            print(a)

            #product_id = Product.objects.get(product_number = row[10]).id 
            #try:
            #    texture_id = Texture.objects.get(name = row[8].capitalize()).id
            #except:
            #    texture_id = None
#            for img in images:
#                Image.objects.create(img_url = img, product_id = product_id)
#            Product.objects.create(category_id=category_id,collection_id = collection_id,stock_status_id = stock_status_id,name=name, price = price, description = description,detail = detail,texture_id = texture_id,color_url = color_url,luggage_color=luggage_color)
    
    for row in data_reader:
        if row:
            
            product_id = Product.objects.get(product_number = row[10]).id
            image_string = row[5][2:len(row[5])-2]
            images = image_string.split("', '")

            for img in images:
                Image.objects.create(img_url = img, product_id = product_id)
            
