import os
import random
import shutil
import csv

from tqdm import tqdm


def writer_to_csvfile(class_name: str, number: int) -> None:
    """Creates a csv file with the replacement of the sequence number of the image with a random one in the range from 0 to 10000

    Args:
        class_name (str): Name of the image class
        number (int): The sequential number of the image
        random_number (int): Random number
    """
    if __name__ == "__main__":
        field_names = ["The Absolute Way", "Relative Way", "Class"]

        with open("dataset_random_dir.csv", "a", newline="", encoding="utf8") as f:
            print_in_csv = csv.DictWriter(
                f, fieldnames=field_names, delimiter=";")

            print_in_csv.writerow({"The Absolute Way": f"C:/Users/User/nuck figgers/dataset_random/{str(number).zfill(5)}.jpg",
                                   "Relative Way": f"dataset_random/{str(number).zfill(5)}.jpg",
                                   "Class": class_name})


def copying_to_new_dir(class_name: str) -> None:
    """Copying images from this directory to a new one

    Args:
        class_name (str): Name of the image class
    """
    if __name__ == "__main__":
        if not os.path.exists("C:/Users/User/nuck figgers/dataset_random"):
            os.mkdir("C:/Users/User/nuck figgers/dataset_random")

    random_list = list(range(0, 10000))
    random.shuffle(random_list)

    for i in tqdm(range(0, 1250)):

        path = f"C:/Users/User/nuck figgers/dataset/{class_name}/{str(i).zfill(4)}.jpg"

        if os.path.isfile(path):
            shutil.copyfile(
                path, f"C:/Users/User/nuck figgers/dataset_random/{str(random_list[i]).zfill(5)}.jpg")

            writer_to_csvfile(class_name, random_list[i])


def main():
    """Maim function"""

    field_names = ["The Absolute Way", "Relative Way", "Class"]

    with open("dataset_random_dir.csv", "w", newline='') as f:
        printer = csv.DictWriter(f, fieldnames=field_names, delimiter=";", )
        printer.writeheader()

    class_name = "cat"
    copying_to_new_dir(class_name)

    class_name = "dog"
    copying_to_new_dir(class_name)


if __name__ == "__main__":
    main()
