import os
import csv
import shutil
from tqdm import tqdm


def copy_to_another_dir(class_name: str, number: int) -> None:
    """Creates a csv file of another directory

    Args:
        class_name (str): Name of the image class
        number (int): The sequential number of the image
    """
    if __name__ == "__main__":
        field_names = ["The Absolute Way", "Relative Way", "Class"]

        with open("dataset_another_dir.csv", "a", newline="", encoding="utf8") as f:
            copy_to_file = csv.DictWriter(
                f, fieldnames=field_names, delimiter=";")

            copy_to_file.writerow({"The Absolute Way": f"C:/Users/User/nuck figgers/dataset_another/{class_name}_{str(number).zfill(4)}.jpg",
                                   "Relative Way": f"dataset_another/{class_name}_{str(number).zfill(4)}.jpg",
                                   "Class": class_name})


def copying_images(class_name: str) -> None:
    """Copies images from this directory to another with the replacement of the name class/0000.jpg on class_0000.jpg 
    and calls the write function in csv file

    Args:
        class_name (str): Name of the image class
    """
    if __name__ == "__main__":
        if not os.path.exists("C:/Users/User/nuck figgers/dataset_another"):
            os.mkdir("C:/Users/User/nuck figgers/dataset_another")

        for i in tqdm(range(0, 1250)):
            path = f"C:/Users/User/nuck figgers/dataset/{class_name}/{str(i).zfill(4)}.jpg"
            if os.path.isfile(path):
                shutil.copyfile(
                    path, f"C:/Users/User/nuck figgers/dataset_another/{class_name}_{str(i).zfill(4)}.jpg")

                copy_to_another_dir(class_name, i)


def main():
    """Main function"""

    field_names = ["The Absolute Way", "Relative Way", "Class"]

    with open("dataset_another_dir.csv", "w", newline='') as f:
        printer = csv.DictWriter(f, fieldnames=field_names, delimiter=";", )
        printer.writeheader()

    class_name = "cat"
    copying_images(class_name)

    class_name = "dog"
    copying_images(class_name)


if __name__ == "__main__":
    main()
