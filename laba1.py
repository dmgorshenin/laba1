import os
import string
import random
import time
from webbrowser import get
import requests
from bs4 import BeautifulSoup
import cv2
import numpy as np
from tqdm import tqdm

dog_path = "C:/Users/User/nuck figgers/dataset/dog"
cat_path = "C:/Users/User/nuck figgers/dataset/cat"

def get_images(count_imgs, path, typename):
    
    if not os.path.exists("C:/Users/User/nuck figgers/dataset"):
        os.mkdir("C:/Users/User/nuck figgers/dataset")
    if not os.path.exists(path):
        os.mkdir(path) 
    
    count=0
    
    for i in tqdm(range(3,999), desc="Страница "):
        
        letters = string.ascii_lowercase
        rand_string = ''.join(random.sample(letters, 10))
        _headers ={
            "User-Agent": rand_string
        }
        
        url = f"https://yandex.ru/images/search?p={i}&text={typename}&"
        req=requests.get(url, headers=_headers)
  
        soup = BeautifulSoup(req.text, "html.parser")

        src_list=[]

        for link in soup.find_all("img", class_="justifier__thumb"):
             src_list.append(link.get("src"))
        
        for img_url in tqdm(src_list, desc="Скчивание картинок "):
            if img_url.find("n=13") !=-1:
                try:
                    source = "https:" + img_url
                    picture = requests.get(source)
                    
                    name_file=str(count)
                    
                    out = open(path + '/' + name_file.zfill(4) + '.jpg', 'wb') 
                    out.write(picture.content)
                    out.close()
                    
                    time.sleep(0.25)
                    
                    count+=1
                    if(count==count_imgs):
                        return
                    
                except Exception:
                    print("Error in: ", count)
                    
                         

def is_similar(image1, image2):
    return image1.shape == image2.shape and not(np.bitwise_xor(image1,image2).any())
    
def check_images(path,count):
    c=count
    images = []
    for filename1 in os.listdir(path):
        images.append((cv2.imread(os.path.join(path, filename1)), os.path.join(path, filename1)))
    
    for im, fname in tqdm(images):
        for im2, fname2 in images:
            if(fname==fname2):
                continue
            if is_similar(im,im2):
                print(fname, fname2)
                os.remove(fname2)
                c-=1;
    return count-c
                
 
 
count_find=1100 

get_images(count_find, dog_path, "dog")

print("Пауза")
for sec in range(1,61):
    print("Осталось ", 61-sec)
    time.sleep(1)
    
get_images(count_find, cat_path, "cat")

new_count=check_images(dog_path,count_find)
get_images(new_count, dog_path, "dog")

print("Пауза")
for sec in range(1,61):
    print("Осталось ", 61-sec)
    time.sleep(1)

new_count=check_images(cat_path,count_find)
get_images(new_count, cat_path, "cat")
