import requests
from bs4 import BeautifulSoup
import lxml
url="https://www.runoob.com/python3/python3-tutorial.html"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0"}
response=requests.get(url,headers=headers)
response.encoding="utf-8"
soup=BeautifulSoup(response.text,'lxml')
title=soup.find('h1').text
contents=soup.find_all('a')
print(title)
print(contents)



