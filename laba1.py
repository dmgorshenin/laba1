import os
import time
import requests
from bs4 import BeautifulSoup

dog_path = "C://Users/User/nuck figgers/dataset/dog"
dataset_path ="C://Users/User/nuck figgers/dataset"
cat_path = "C://Users/User/nuck figgers/dataset/cat"


def get_data_dog(count_imgs):
    
    _headers ={
        "User-Agent": "Dima"
    }
    
    count=0
    
    for i in range(0,10):
        
        url = f"https://yandex.ru/images/search?p={i}&text=dog&uinfo=sw-1920-sh-1080-ww-912-wh-881-pd-1.100000023841858-wp-16x9_2560x1440&lr=51&rpt=image"
        req=requests.get(url, headers=_headers)
  
        soup = BeautifulSoup(req.text, "html.parser")

        src_list=[]
        
        try:
            for link in soup.find_all("img", class_="justifier__thumb"):
                src_list.append(link.get("src"))
            print("Картинки успешно сканированы")
        
        except Exception:
            print("Нет картинок")
        
        
        for img_url in src_list:
            if img_url.find("n=13") !=-1:
                try:
                    source = "https:" + img_url
                    picture = requests.get(source)
                    
                    if not os.path.exists(dataset_path):
                        os.mkdir(dataset_path)   
                    if not os.path.exists(dog_path):
                            os.mkdir(dog_path)  
                    
                    name_file=str(count)
                          
                    out = open(dog_path + '/' + name_file.zfill(4) + '.jpg', 'wb') 
                    out.write(picture.content)
                    out.close()
                    
                    count+=1
                    if(count==count_imgs):
                        return
                    
                except Exception:
                    print("Error in: ", count)
        

        for sec in range(1,61):
            print("Осталось ", 60-sec)
            time.sleep(1)
                    
       
    
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
        images = soup.fin_all("img", class_ ="justifier__thumb")
    
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

 
count_find=100   
get_data_dog(count_find)
#get_data_cat("https://yandex.ru/images/search?text=cat")