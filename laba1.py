from webbrowser import get
from bs4 import BeautifulSoup
import requests
import re
from re import sub
from decimal import Decimal
import io
from datetime import datetime
import pandas as pd
import os
import cv2
import pyautogui

dog_path = "C://Users/User/nuck figgers/dataset/dog"
dataset_path ="C://Users/User/nuck figgers/dataset"
cat_path = "C://Users/User/nuck figgers/dataset/cat"

def key_creater(key):
    d = ['']
    j=0
    for i in range(10):
      for g in range(10):
          for k in range(10):
            d.append(str(j)+str(i)+str(g)+str(k))
    return d[key]
            
        

def get_data_dog(url):
    headers ={
        "user-agent":"Dima"
    } 
    
    
    req=requests.get(url,headers)
    with open("dogs.html", "w", encoding="utf-8") as file:
         file.write(req.text)
         
    with open("dogs.html", encoding="utf-8") as file:
        src = file.read()
        
    soup = BeautifulSoup(src, "lxml")
    try:
        images = soup.find_all("img", class_ ="justifier__thumb")
    
    except Exception:
        images = "Нет картинок"
    
    count = 1
    for img in images:
        
        url = img['src']
        source = "https:" + url
        picture = requests.get(source)
        
        if not os.path.exists(dataset_path):
            os.mkdir(dataset_path)   
        if not os.path.exists(dog_path):
                os.mkdir(dog_path)  
                      
        out = open(dog_path + '/' + str(key_creater(count)) + '.jpg', 'wb') 
        out.write(picture.content)
        out.close()
        
        count+=1
        
    
def get_data_cat(url):
    headers ={
        "user-agent":"Dima"
    } 
    
    req=requests.get(url,headers)
    with open("cats.html", "w", encoding="utf-8") as file:
         file.write(req.text)
         
    with open("cats.html", encoding="utf-8") as file:
        src = file.read()
        
    soup = BeautifulSoup(src, "lxml")
    
    try: 
        images = soup.find_all("img", class_ ="justifier__thumb")
    
    except Exception:
        images = "Нет картинок"
    
    
    count = 1
    for img in images:
        
        url = img['src']
        source = "https:" + url
        picture = requests.get(source)
        
        if not os.path.exists(dataset_path):
            os.mkdir(dataset_path)   
        if not os.path.exists(cat_path):
                os.mkdir(cat_path)  
                      
        out = open(cat_path + '/' + str(key_creater(count)) + '.jpg', 'wb') 
        out.write(picture.content)
        out.close()
        
        count += 1
        
get_data_dog("https://yandex.ru/images/search?text=%20dog")
get_data_cat("https://yandex.ru/images/search?text=cat")










# _url = 'https://yandex.ru/images/search?text=%20dog'
# _html_page = requests.get(_url, headers={'User-Agent':'Dima'}).text
# _soup = BeautifulSoup(_html_page, 'lxml')
# _ad = _soup.find_all('img', class_ = 'serp-item__thumb justifier__thumb')


# count = 0
# for i in range(len(_ad)):
#     if _ad[i]['src']:
#         count += 1 


# #os.mkdir('C://Users/User/nuck figgers/dataset/cat')


# _https = 'https:'
# _dog_path = 'C://Users/User/nuck figgers/dataset/dog'
# for i in range(count):
#     _src = _https + _ad[i]['src']
#     _picture = requests.get(_src)
#     if not os.path.exists(_dog_path):
#          os.mkdir(_dog_path)
#     out = open(_dog_path + '/' + str(i) + '.jpg', 'wb') 
#     out.write(_picture.content)
#     out.close()

