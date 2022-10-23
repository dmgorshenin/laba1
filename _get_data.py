from _iterator import Iterator
from tqdm import tqdm

def main():
    path_to_file="C:/Users/User/nuck figgers/dataset.csv"
    path_to_another_dir="C:/Users/User/nuck figgers/dataset_another_dir.csv"
    path_to_random="C:/Users/User/nuck figgers/dataset_random_dir.csv"
    class_name_cat="cat"
    class_name_dog="dog"
    a=Iterator(path_to_random, class_name_dog)
    
    try:
        for i in tqdm(a):
            print(i)
        # next(a)
        # print(next(a))
    except Exception as e:
        print(e)

if __name__=="__main__":
    main()    