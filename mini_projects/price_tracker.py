import requests
from bs4 import BeautifulSoup

def get_product_price(url):
    headers ={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
    }

    page = requests.get(url, headers= headers)
    page_content = BeautifulSoup(page.content, 'html.parser')
    google_pixel_price = page_content.find(class_="_30jeq3 _16Jk6d")
    return google_pixel_price.getText()

product_list = [
    {
        'name':'google pixel 7a',
        'url':'https://www.flipkart.com/google-pixel-7a-charcoal-128-gb/p/itmb4d7b100b1a4d?pid=MOBGZCQMHGWDYZQ7&lid=LSTMOBGZCQMHGWDYZQ7ORMHQK&marketplace=FLIPKART&q=google+pixel+7a&store=tyy%2F4io&srno=s_1_1&otracker=AS_QueryStore_OrganicAutoSuggest_1_10_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_1_10_na_na_ps&fm=search-autosuggest&iid=14e31c58-5eee-4bd4-84b4-322d6088ecde.MOBGZCQMHGWDYZQ7.SEARCH&ppt=sp&ppn=sp&ssid=jcdk6908kw0000001692112448311&qH=51245925943291b1',
        'expected_price':38000
    },
{
        'name':'asus rog phone 2',
        'url':'https://www.flipkart.com/asus-rog-phone-ii-black-128-gb/p/itm99be8e028a908?pid=MOBFK5TPW6UFVZGR&lid=LSTMOBFK5TPW6UFVZGRXVURJG&marketplace=FLIPKART&q=asus+rog+phone&store=tyy%2F4io&srno=s_1_1&otracker=AS_Query_OrganicAutoSuggest_2_12_na_na_ps&otracker1=AS_Query_OrganicAutoSuggest_2_12_na_na_ps&fm=Search&iid=2971a218-85e6-4b83-a29a-79af39b8e136.MOBFK5TPW6UFVZGR.SEARCH&ppt=sp&ppn=sp&ssid=tl41mmjqz40000001692194380891&qH=84219e54f34cba73',
        'expected_price':35000
    },
{
        'name':'samsung galaxy note 20',
        'url':'https://www.flipkart.com/samsung-galaxy-note-20-mystic-green-256-gb/p/itm38acf149a4551?pid=MOBFU5WYVAAGDCGW&lid=LSTMOBFU5WYVAAGDCGWKJD8SS&marketplace=FLIPKART&q=samsung+galaxy+note&store=tyy%2F4io&srno=s_1_1&otracker=search&otracker1=search&fm=Search&iid=f69b7c3b-7f08-449a-a666-6921607be252.MOBFU5WYVAAGDCGW.SEARCH&ppt=sp&ppn=sp&ssid=bncz90m8b40000001692195932124&qH=de02224da9f956a0',
        'expected_price':75000
    },
{
        'name':'iPhone 14',
        'url':'https://www.flipkart.com/apple-iphone-14-midnight-128-gb/p/itm9e6293c322a84?pid=MOBGHWFHECFVMDCX&lid=LSTMOBGHWFHECFVMDCXSSCYWA&marketplace=FLIPKART&q=iphone+14&store=tyy%2F4io&srno=s_1_1&otracker=AS_QueryStore_OrganicAutoSuggest_2_2_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_2_2_na_na_ps&fm=Search&iid=34a536f3-2a96-41b5-af9f-77a6963478f8.MOBGHWFHECFVMDCX.SEARCH&ppt=sp&ppn=sp&ssid=g5l81oxrk00000001692199491215&qH=860f3715b8db08cd',
        'expected_price':60000
    },
{
        'name':'Nothing phone 2',
        'url':'https://www.flipkart.com/nothing-phone-2-dark-grey-512-gb/p/itmc1490711c3eb9?pid=MOBGZSDKJSFH7GZT&lid=LSTMOBGZSDKJSFH7GZT0NUNZF&marketplace=FLIPKART&q=nothing+mobile&store=tyy%2F4io&srno=s_1_9&otracker=AS_Query_OrganicAutoSuggest_3_7_na_na_ps&otracker1=AS_Query_OrganicAutoSuggest_3_7_na_na_ps&fm=search-autosuggest&iid=89d3d407-d891-4661-99d2-46446215a9fb.MOBGZSDKJSFH7GZT.SEARCH&ppt=sp&ppn=sp&ssid=vfgtosphzk0000001692199615999&qH=d89568c12cf8689a',
        'expected_price':55500
    }
]

result_file = open('price_tracker_results','w')
try:
    for every_product in product_list:
        print(f'Price of {every_product.get("name")} is: {get_product_price(every_product.get("url"))}')
        product_price = int(get_product_price(every_product.get('url')).replace('₹', '').replace(',', ''))

        if product_price <= every_product.get('expected_price'):
            print(f'Hurry up the price of {every_product.get("name")} lies in your expected price and you can buy it!\n')
            result_file.write(f'Hurry up the price of {every_product.get("name")} lies in your expected price and you can buy it!\n')

        else:
            print(f'{every_product.get("name")} is still not in your expected range\n')

finally:
    result_file.close()

