import os
import csv
import shutil
from tqdm import tqdm


def copy_to_another_dir(class_name: str, number: int, new_path: str) -> None:
    """Creates a csv file of another directory

    Args:
        class_name (str): Name of the image class
        number (int): The sequential number of the image
        csv_file (str): Name of the csvfile
        path_to_dir (str): Path to the another directory

    Raises:
        NotFoundErr: If the file extension is not csv , an exception is raised
    """
    if __name__ == "__main__":
        field_names = ["The Absolute Way", "Relative Way", "Class"]

        with open("dataset_another_dir.csv", "a", newline="", encoding="utf8") as f:
            copy_to_file = csv.DictWriter(
                f, fieldnames=field_names, delimiter=";")

            copy_to_file.writerow({"The Absolute Way": new_path,
                                   "Relative Way": f"dataset_another/{class_name}_{str(number).zfill(4)}.jpg",
                                   "Class": class_name})


def copying_images(path_to_another_dir: str, path_to_dataset: str) -> None:
    """Copies images from this directory to another with the replacement of the name class/0000.jpg on class_0000.jpg 
    and calls the write function in csv file

    Args:
        class_name (str): Name of the image class
        csv_file (str): Name of the csvfile
        path_to_dir (str): Path to the another directory
    """
    if __name__ == "__main__":
        if not os.path.exists(path_to_another_dir):
            os.mkdir(path_to_another_dir)

        field_names = ["The Absolute Way", "Relative Way", "Class"]
        with open("dataset_another_dir.csv", "w", newline="", encoding="utf8") as f:
            printer = csv.DictWriter(f, fieldnames=field_names, delimiter=";")
            printer.writeheader()

        class_name = "cat"
        path_to_cat = path_to_dataset + "/"+class_name
        num_files = len([f for f in os.listdir(path_to_cat)
                         if os.path.isfile(os.path.join(path_to_cat, f))])

        for i in tqdm(range(0, num_files)):
            path = path_to_cat + f"/{str(i).zfill(4)}.jpg"
            new_path = path_to_another_dir + \
                f"/{class_name}_{str(i).zfill(4)}.jpg"
                
            if os.path.isfile(path):
                shutil.copyfile(path, new_path)

                copy_to_another_dir(class_name, i, new_path)

        class_name = "dog"
        path_to_dog = path_to_dataset + "/"+class_name
        num_files = len([f for f in os.listdir(path_to_dog)
                         if os.path.isfile(os.path.join(path_to_dog, f))])

        for i in tqdm(range(0, num_files)):
            path = path_to_dog + f"/{str(i).zfill(4)}.jpg"
            new_path = path_to_another_dir + \
                f"/{class_name}_{str(i).zfill(4)}.jpg"
                
            if os.path.isfile(path):
                shutil.copyfile(path, new_path)

                copy_to_another_dir(class_name, i, new_path)


def main():
    """Main function"""
    path_to_another_dir = "C:/Users/User/nuck figgers/dataset_another"
    path_to_dataset = "C:/Users/User/nuck figgers/dataset"

    copying_images(path_to_another_dir, path_to_dataset)


if __name__ == "__main__":
    main()
