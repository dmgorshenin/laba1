import os
import random
import shutil
import csv

from tqdm import tqdm


def writer_to_csvfile(class_name: str, number: int, new_path: str) -> None:
    """Creates a csv file with the replacement of the sequence number of the image with a random one in the range from 0 to 10000

    Args:
        class_name (str): Name of the image class
        number (int): Random number
        csv_file (str): Name of the csvfile
        path_to_dir (str): Path to the another directory with random names

    Raises:
        NotFoundErr: If the file extension is not csv , an exception is raised
    """
    if __name__ == "__main__":
        field_names = ["The Absolute Way", "Relative Way", "Class"]

        with open("dataset_random_dir.csv", "a", newline="", encoding="utf8") as f:
            print_in_csv = csv.DictWriter(
                f, fieldnames=field_names, delimiter=";")

            print_in_csv.writerow({"The Absolute Way": new_path,
                                   "Relative Way": f"dataset_random/{str(number).zfill(5)}.jpg",
                                   "Class": class_name})


def copying_to_random(path_to_dataset: str, path_to_random_dir: str, csv_path: str = "") -> str or None:
    """Copying images from the dataset directory to a new one and creates a csv file with the replacement 
    of the sequence number of the image with a random one in the range from 0 to 10000

    Args:
        path_to_dataset (str): Path to the dataset
        path_to_random_dir (str): Path to the another directory with random number of the image 
        csv_path (str, optional): Name of the csvfile. Defaults to "".

    Returns:
        str or None: Returns path to csvfile or None 
    """

    if not csv_path.find(".csv"):
        if not os.path.exists(path_to_random_dir):
            os.mkdir(path_to_random_dir)

        field_names = ["The Absolute Way", "Relative Way", "Class"]
        with open(csv_path, "w", newline="", encoding="utf8") as f:
            printer = csv.DictWriter(
                f, fieldnames=field_names, delimiter=";", )
            printer.writeheader()

        random_list = list(range(0, 10001))
        random.shuffle(random_list)
        random_list1 = random_list[:len(random_list)//2]
        random_list2 = random_list[len(random_list)//2:]

        class_name = "cat"
        path_to_cat = os.path.join(path_to_dataset, class_name)
        num_files = len([f for f in os.listdir(path_to_cat)
                        if os.path.isfile(os.path.join(path_to_cat, f))])

        for i in tqdm(range(0, num_files)):
            path = os.path.join(path_to_cat, f"{str(i).zfill(4)}.jpg")
            new_path = os.path.join(
                path_to_random_dir, f"{str(random_list1[i]).zfill(5)}.jpg")

            if os.path.isfile(path):
                shutil.copyfile(path, new_path)

                with open(csv_path, "a", newline="", encoding="utf8") as f:
                    print_in_csv = csv.DictWriter(
                        f, fieldnames=field_names, delimiter=";")

                    print_in_csv.writerow({"The Absolute Way": new_path,
                                           "Relative Way": os.path.relpath(new_path),
                                           "Class": class_name})

        class_name = "dog"
        path_to_dog = os.path.join(path_to_dataset, class_name)
        num_files = len([f for f in os.listdir(path_to_dog)
                        if os.path.isfile(os.path.join(path_to_dog, f))])

        for i in tqdm(range(0, num_files)):
            path = os.path.join(path_to_dog, f"{str(i).zfill(4)}.jpg")
            new_path = os.path.join(
                path_to_random_dir, f"{str(random_list2[i]).zfill(5)}.jpg")
            if os.path.isfile(path):
                shutil.copyfile(path, new_path)

                with open(csv_path, "a", newline="", encoding="utf8") as f:
                    print_in_csv = csv.DictWriter(
                        f, fieldnames=field_names, delimiter=";")

                    print_in_csv.writerow({"The Absolute Way": new_path,
                                           "Relative Way": os.path.relpath(new_path),
                                           "Class": class_name})

    else:
        if not os.path.exists(path_to_random_dir):
            os.mkdir(path_to_random_dir)

        field_names = ["The Absolute Way", "Relative Way", "Class"]
        with open(os.path.join(path_to_random_dir, "_dataset_random_dir.csv"), "w", newline="", encoding="utf8") as f:
            printer = csv.DictWriter(
                f, fieldnames=field_names, delimiter=";", )
            printer.writeheader()

        random_list = list(range(0, 10001))
        random.shuffle(random_list)
        random_list1 = random_list[:len(random_list)//2]
        random_list2 = random_list[len(random_list)//2:]

        class_name = "cat"
        path_to_cat = os.path.join(path_to_dataset, class_name)
        num_files = len([f for f in os.listdir(path_to_cat)
                        if os.path.isfile(os.path.join(path_to_cat, f))])

        for i in tqdm(range(0, num_files)):
            path = os.path.join(path_to_cat, f"{str(i).zfill(4)}.jpg")
            new_path = os.path.join(
                path_to_random_dir, f"{str(random_list1[i]).zfill(5)}.jpg")

            if os.path.isfile(path):
                shutil.copyfile(path, new_path)

                with open(os.path.join(path_to_random_dir, "_dataset_random_dir.csv"), "a", newline="", encoding="utf8") as f:
                    print_in_csv = csv.DictWriter(
                        f, fieldnames=field_names, delimiter=";")

                    print_in_csv.writerow({"The Absolute Way": new_path,
                                           "Relative Way": os.path.relpath(new_path),
                                           "Class": class_name})

        class_name = "dog"
        path_to_dog = os.path.join(path_to_dataset, class_name)
        num_files = len([f for f in os.listdir(path_to_dog)
                        if os.path.isfile(os.path.join(path_to_dog, f))])

        for i in tqdm(range(0, num_files)):
            path = os.path.join(path_to_dog, f"{str(i).zfill(4)}.jpg")
            new_path = os.path.join(
                path_to_random_dir, f"{str(random_list2[i]).zfill(5)}.jpg")

            if os.path.isfile(path):
                shutil.copyfile(path, new_path)

                with open(os.path.join(path_to_random_dir, "_dataset_random_dir.csv"), "a", newline="", encoding="utf8") as f:
                    print_in_csv = csv.DictWriter(
                        f, fieldnames=field_names, delimiter=";")

                    print_in_csv.writerow({"The Absolute Way": new_path,
                                           "Relative Way": os.path.relpath(new_path),
                                           "Class": class_name})

        return os.path.join(path_to_random_dir, "_dataset_random_dir.csv")


def main():
    """Main function"""
    path_to_random_dir = "C:/Users/User/nuck figgers/dataset_random"
    path_to_dataset = "C:/Users/User/nuck figgers/dataset"
    csv_path = "dataset_random_dir.csv"

    copying_to_random(path_to_random_dir, path_to_dataset, csv_path)


if __name__ == "__main__":
    main()
