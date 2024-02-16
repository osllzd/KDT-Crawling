import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from urllib.request import urlopen
from urllib.request import Request
html =urlopen("https://www.news1.kr/articles/5315281")
soup = BeautifulSoup(html.read().decode('utf-8'), 'html.parser')
# 기사 제목만 뽑아내기
food_title = soup.find("div", {"class":"title"})
food_title1 = food_title.select('h2')
food_title1 = str(food_title1)
print(food_title1[5:-7])
print('-'*100)
# 기사 내용만 뽑아내기
food_list = soup.find_all("div",{"class":"detail sa_area"})
for idx in range(len(food_list)):
    print(food_list[idx].text)


