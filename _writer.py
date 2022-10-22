import csv
from operator import truediv
import os

from tqdm import tqdm


def write_to_file(class_name: str, number: int) -> None:
    """Write paths to csv file

    Args:
        class_name (str): Name of the image class
        number (int): The sequential number of the image
    """
    if __name__ == "__main__":
        field_names = ["The Absolute Way", "Relative Way", "Class"]
        
        with open("dataset.csv", "a", newline="", encoding="utf8") as f:
            print_in_file = csv.DictWriter(
                f, fieldnames=field_names, delimiter=";")

            path = f"dataset/{class_name}/{str(number).zfill(4)}.jpg"

            if os.path.isfile(path):
                print_in_file.writerow({"The Absolute Way": f"C:/Users/User/nuck figgers/dataset/{class_name}/{str(number).zfill(4)}.jpg",
                                        "Relative Way": f"dataset/{class_name}/{str(number).zfill(4)}.jpg",
                                        "Class": class_name})


def main() -> None:
    """Main function"""
    field_names = ["The Absolute Way", "Relative Way", "Class"]

    with open("dataset_random_dir.csv", "w", newline='') as f:
        printer = csv.DictWriter(f, fieldnames=field_names, delimiter=";", )
        printer.writeheader()
    
    for i in tqdm(range(0,1250)):
        class_name = "cat"
        write_to_file(class_name, i)

    for i in tqdm(range(0,1250)):
        class_name="dog"
        write_to_file(class_name, i)



if __name__ == "__main__":
    main()
