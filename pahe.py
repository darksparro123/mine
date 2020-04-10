import requests

from bs4 import BeautifulSoup

web_request = requests.get("https://pahe.me/bad-boys-for-life-2020/")

web_content = web_request.content

web_content = BeautifulSoup(web_content)

find_result = web_content.find_all("a" , href = True)

for items in find_result :

    link = items["href"]

    item_text = items.text

    items_text_2 = items.text

    item_text = item_text.split(" ")

    if item_text[0] == "MG" or item_text[0] =="GD" :

        print (items_text_2,"  ",link) 