import requests

URL ='https://www.flipkart.com/google-pixel-7a-charcoal-128-gb/p/itmb4d7b100b1a4d?pid=MOBGZCQMHGWDYZQ7&lid=LSTMOBGZCQMHGWDYZQ7ORMHQK&marketplace=FLIPKART&q=google+pixel+7a&store=tyy%2F4io&srno=s_1_1&otracker=AS_QueryStore_OrganicAutoSuggest_1_10_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_1_10_na_na_ps&fm=search-autosuggest&iid=14e31c58-5eee-4bd4-84b4-322d6088ecde.MOBGZCQMHGWDYZQ7.SEARCH&ppt=sp&ppn=sp&ssid=jcdk6908kw0000001692112448311&qH=51245925943291b1'

headers ={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}

page = requests.get(URL, headers= headers)

print(page)