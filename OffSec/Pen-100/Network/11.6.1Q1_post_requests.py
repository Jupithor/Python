#!/usr/bin/python3
#html parser

from inspect import Parameter
import requests
from bs4 import BeautifulSoup 

host='http://192.168.99.68:8080'
subpage='/basic-post'

#Data to send to server
info={"Offsec": "Offsec"}


post = requests.post(host+subpage,data = info)
print(post.status_code)
print(post.text)