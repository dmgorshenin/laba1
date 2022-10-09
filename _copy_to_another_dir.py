import os
import csv
import shutil
from tqdm import tqdm


def copying_images(class_name: str) -> None:
    """Copies images from this directory to another with the replacement of the name class/0000.jpg on class_0000.jpg

    Args:
        class_name (str): Name of the image class
    """
    if __name__ == "__main__":
        if not os.path.exists("C:/Users/User/nuck figgers/dataset_another"):
            os.mkdir("C:/Users/User/nuck figgers/dataset_another")

        for i in tqdm(range(0, 1100)):
            path = f"C:/Users/User/nuck figgers/dataset/{class_name}/{str(i).zfill(4)}.jpg"
            if os.path.isfile(path):
                shutil.copyfile(
                    path, f"C:/Users/User/nuck figgers/dataset_another/{class_name}_{str(i).zfill(4)}.jpg")


def main():
    """Main function"""
    with open("dataset_another.csv", "w", newline="", encoding="utf8") as f:
        print_to_another = csv.writer(f, delimiter=";")
        print_to_another.writerow(
            ["The Absolute Way", "Relative Way", "Class"])

    class_name = "cat"
    copying_images(class_name)

    class_name = "dog"
    copying_images(class_name)


if __name__ == "__main__":
    main()
