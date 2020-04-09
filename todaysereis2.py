import requests

from bs4 import BeautifulSoup

user_request = str (input ("Enter Your link Here : "))

requset = requests.get (user_request)

web_content = requset.content

#print ( web_content)

suop_content = BeautifulSoup (web_content)

#print (suop_content)

a_tags = suop_content.find_all("a" , href = True)

for items in a_tags :

    item_text = items.text

    item_text_dublicate  = items.text

    link = items ["href"]

    #print (item_text)
    item_text = item_text.split (" ")

    if item_text[0] == "Download" :

        print (item_text_dublicate," ",link)



