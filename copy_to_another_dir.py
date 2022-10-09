import os
import csv
import shutil
from this import d
from tqdm import tqdm


def copy_to_another_dir(class_name: str, number: int) -> None:
    if __name__ == "__main__":
        with open("dataset_another.csv", "a", newline="", encoding="utf8") as f:
            copy_to_file = csv.writer(f, delimiter=";")
            copy_to_file.writerow([f"C:/Users/User/nuck figgers/dataset_another/{class_name}_{str(number).zfill(4)}.jpg",
                                   f"dataset_another/{class_name}_{str(number).zfill(4)}.jpg",
                                   class_name])


def copying_images(class_name: str) -> None:
    if __name__ == "__main__":
        if not os.path.exists("C:/Users/User/nuck figgers/dataset_another"):
            os.mkdir("C:/Users/User/nuck figgers/dataset_another")

        for i in tqdm(range(0, 1100)):
            path = f"C:/Users/User/nuck figgers/dataset/{class_name}/{str(i).zfill(4)}.jpg"
            if os.path.isfile(path):
                shutil.copyfile(
                    path, f"C:/Users/User/nuck figgers/dataset_another/{class_name}_{str(i).zfill(4)}.jpg")
                copy_to_another_dir(class_name, i)


def main():
    with open("dataset_another.csv", "w", encoding="utf8") as f:
        print_to_another = csv.writer(f, delimiter=";")
        print_to_another.writerow(
            ["The Absolute Way", "Relative Way", "Class"])

    class_name = "cat"
    copying_images(class_name)

    class_name = "dog"
    copying_images(class_name)


if __name__ == "__main__":
    main()
