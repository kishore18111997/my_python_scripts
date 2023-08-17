import pandas
import openpyxl
import requests
from bs4 import BeautifulSoup

def get_product_price(url):
    headers ={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
    }

    page = requests.get(url, headers= headers)
    page_content = BeautifulSoup(page.content, 'html.parser')
    product_price = page_content.find(class_="_30jeq3 _16Jk6d")
    return product_price.getText()

data_file_path = 'product_sheet.xlsx'
df = pandas.read_excel(data_file_path)
product_list = df.values.tolist()

result_file = open('price_tracker_results','w')

try:
    for every_product in product_list:
        print(f'Price of {every_product[0]} is: {get_product_price(every_product[1])}')
        product_price = int(get_product_price(every_product[1]).replace('₹', '').replace(',', ''))

        if product_price <= every_product[2]:
            print(f'Hurry up the price of {every_product[0]} lies in your expected price and you can buy it!\n')
            result_file.write(f'Hurry up the price of {every_product[0]} lies in your expected price and you can buy it!\n')

        else:
            print(f'{every_product[0]} is still not in your expected range\n')

finally:
    result_file.close()
