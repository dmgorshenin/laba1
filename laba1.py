import os
import string
import random
import time
import requests
from bs4 import BeautifulSoup
import cv2
import numpy as np

dog_path = "C://Users/User/nuck figgers/dataset/dog"
dataset_path ="C://Users/User/nuck figgers/dataset"
cat_path = "C://Users/User/nuck figgers/dataset/cat"


def get_data_dog(count_imgs):
    
    if not os.path.exists(dataset_path):
        os.mkdir(dataset_path)   
    if not os.path.exists(dog_path):
        os.mkdir(dog_path)
    
    count=0
    
    for i in range(0,999):
        
        letters = string.ascii_lowercase
        rand_string = ''.join(random.sample(letters, 10))
        
        _headers ={
            "User-Agent": rand_string
        }
        
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
                    print("Картинка", count)
                    source = "https:" + img_url
                    picture = requests.get(source)
                    
                      
                    
                    name_file=str(count)
                          
                    out = open(dog_path + '/' + name_file.zfill(4) + '.jpg', 'wb') 
                    out.write(picture.content)
                    out.close()
                    
                    time.sleep(0.25)
                    
                    count+=1
                    if(count==count_imgs):
                        return
                    
                except Exception:
                    print("Error in: ", count)
                    
       
    
def get_data_cat(count_imgs):
    
    if not os.path.exists(dataset_path):
        os.mkdir(dataset_path)   
    if not os.path.exists(cat_path):
        os.mkdir(cat_path)
        
    count=0
    
    for i in range(0,999):
        
        letters = string.ascii_lowercase
        rand_string = ''.join(random.sample(letters, 10))
        _headers ={
            "user-agent":rand_string
        } 
        
        url = f"https://yandex.ru/images/search?p={i}&text=cat&uinfo=sw-1920-sh-1080-ww-878-wh-924-pd-1-wp-16x9_1920x1080&lr=51&rpt=image"
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
                    print("Картинка", count)
                    source = "https:" + img_url
                    picture = requests.get(source)
                    
                    name_file=str(count)
                          
                    out = open(cat_path + '/' + name_file.zfill(4) + '.jpg', 'wb') 
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
    import tqdm
    c=count
    images = []
    for filename1 in os.listdir(path):
        images.append((cv2.imread(os.path.join(path, filename1)), os.path.join(path, filename1)))
    
    for im, fname in tqdm.tqdm(images):
        for im2, fname2 in images:
            if(fname==fname2):
                continue
            if is_similar(im,im2):
                print(fname, fname2)
                os.remove(fname2)
                c-=1;
    return count-c
                
    
    #for filename1 in tqdm.tqdm(os.listdir(path)):
    #    img1=cv2.imread(os.path.join(path, filename1))
    #    for filename2 in os.listdir(path):
    #        img2=cv2.imread(os.path.join(path, filename2))
    #        
    #        if(filename1==filename2):
    #            continue
    #        
    #        if is_similar(img1,img2):
    #            print(filename1, filename2)
    #            #os.remove(filename2)
            
    



 
 
count_find=1100 

get_data_dog(count_find)

print("Пауза")
for sec in range(1,61):
    print("Осталось ", 61-sec)
    time.sleep(1)

get_data_cat(count_find)

new_count=check_images(dog_path,count_find)
get_data_cat(new_count)
new_count=check_images(cat_path,count_find)
get_data_dog(new_count)
