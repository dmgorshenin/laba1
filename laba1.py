from logging import exception
import os
import random
import string
import time

import cv2
import numpy as np
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

dog_path = "C:/Users/User/nuck figgers/dataset/dog"
cat_path = "C:/Users/User/nuck figgers/dataset/cat"


def get_images(count_imgs, path, typename, indexs=None, page_count=0):

    if not os.path.exists("C:/Users/User/nuck figgers/dataset"):
        os.mkdir("C:/Users/User/nuck figgers/dataset")
    if not os.path.exists(path):
        os.mkdir(path)

    count = 0

    for i in tqdm(range(page_count, 99), desc="Страница "):

        letters = string.ascii_lowercase
        rand_string = ''.join(random.sample(letters, 7))
        _headers = {
            "User-Agent": rand_string
        }
        if not typename == "cat":
            url = f"https://yandex.ru/images/search?p={i}&text=dog&uinfo=sw-1920-sh-1080-ww-912-wh-881-pd-1.100000023841858-wp-16x9_2560x1440&lr=51&rpt=image"
        else:
            url = f"https://yandex.ru/images/search?p={i}&text=cat&uinfo=sw-1920-sh-1080-ww-878-wh-924-pd-1-wp-16x9_1920x1080&lr=51&rpt=image"

        req = requests.get(url, headers=_headers)

        soup = BeautifulSoup(req.text, "html.parser")

        src_list = []

        for link in soup.find_all("img", class_="justifier__thumb"):
            src_list.append(link.get("src"))

        for img_url in tqdm(src_list, desc="Скчивание картинок "):
            if img_url.find("n=13") != -1:
                try:
                    source = "https:" + img_url
                    picture = requests.get(source)

                    if indexs != None:
                        name_file = str(indexs[count])
                    else:
                        name_file = str(count)

                    out = open(path + '/' + name_file.zfill(4) + '.jpg', 'wb')
                    out.write(picture.content)
                    out.close()

                    time.sleep(0.5)

                    count += 1
                    if(count == count_imgs):
                        return i

                except Exception:
                    print("Error in: ", count)


def is_similar(image1, image2):
    return image1.shape == image2.shape and not(np.bitwise_xor(image1, image2).any())


def check_images(path):
    c = 0
    images = []
    images2 = []
    for file_name in os.listdir(path):
        images.append((cv2.imread(os.path.join(path, file_name)),
                      os.path.join(path, file_name)))

        images2.append((cv2.imread(os.path.join(path, file_name)),
                        os.path.join(path, file_name)))

    indexs = []
    for im, fname in tqdm(images):
        for im2, fname2 in images2:
            if(fname == fname2):
                continue
            
            if is_similar(im, im2):
                print(fname, fname2)
                
                try:
                    os.remove(fname)
                except Exception as e:
                    print(e)
                    
                temp = fname.replace(f"{path}\\", "")
                temp = temp.replace(".jpg", "")
                indexs.append(int(temp))
                
                try:
                    images2.remove(fname2)
                except Exception:
                    continue

                c += 1
    return c, indexs


def main():
    count_find = 1250

    page_number_dog = get_images(count_find, dog_path, "dog")

    print("Пауза")
    for sec in tqdm(range(1, 121), ):
        time.sleep(1)

    page_number_cat = get_images(count_find, cat_path, "cat")

    new_count, indexs = check_images(dog_path)
    get_images(new_count, dog_path, "dog", indexs, page_number_dog)

    print("Пауза")
    for sec in range(1, 61):
        print("Осталось ", 61-sec)
        time.sleep(1)

    new_count, indexs = check_images(cat_path)
    get_images(new_count, cat_path, "cat", indexs, page_number_cat)


if __name__ == "__main__":
    main()
