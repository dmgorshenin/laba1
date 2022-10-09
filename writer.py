import csv
import os

import numpy as np
from tqdm import tqdm


def write_to_file(class_name: str, number: int) -> None:
    """Write paths to csv file

    Args:
        class_name (str): Name of the image class
        number (int): The sequential number of the image
    """
    if __name__ == "__main__":
        with open("dataset.csv", "a", newline="", encoding="utf8") as f:
            print_in_file = csv.writer(f, delimiter=";")
            print_in_file.writerow([f"C:/Users/User/nuck figgers/dataset/{class_name}/{str(number).zfill(4)}.jpg",
                                    f"dataset/{class_name}/{str(number).zfill(4)}.jpg",
                                    class_name])


def main() -> None:
    """Main function"""
    
    with open("dataset.csv", "w", newline='') as f:
        printer = csv.writer(f, delimiter=";", )
        printer.writerow(["The Absolute Way", "Relative Way", "Class"])

    for i in tqdm(range(0, 1100)):
        class_name = "cat"
        path = f"dataset/{class_name}/{str(i).zfill(4)}.jpg"

        if os.path.isfile(path):
            write_to_file(class_name, i)

    for i in tqdm(range(0, 1100)):
        class_name = "dog"
        path = f"dataset/{class_name}/{str(i).zfill(4)}.jpg"

        if os.path.isfile(path):
            write_to_file(class_name, i)


if __name__ == "__main__":
    main()
