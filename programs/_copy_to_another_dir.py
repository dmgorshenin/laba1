import os
import csv
import shutil
from tqdm import tqdm


def copying_images_to_another(path_to_dataset: str, path_to_another_dir: str, csv_path: str = "") -> str or None:
    """Copies images from this directory to another with the replacement of the name class/0000.jpg on class_0000.jpg 
    and calls the write function in csv file
    
    Args:
        path_to_dataset (str): Path to the dataset
        path_to_another_dir (str): Path to the another new directory
        csv_path (str, optional): Name of the csvfile. Defaults to "".

    Returns:
        str or None: Returns path to csvfile or None 
    """
    if not csv_path.find(".csv"):
        if not os.path.exists(path_to_another_dir):
            os.mkdir(path_to_another_dir)

        field_names = ["The Absolute Way", "Relative Way", "Class"]
        with open(csv_path, "w", newline="", encoding="utf8") as f:
            printer = csv.DictWriter(
                f, fieldnames=field_names, delimiter=";")
            printer.writeheader()

        class_name = "cat"
        path_to_cat = os.path.join(path_to_dataset, class_name)
        num_files = len([f for f in os.listdir(path_to_cat)
                        if os.path.isfile(os.path.join(path_to_cat, f))])

        for i in tqdm(range(0, num_files)):
            path = os.path.join(path_to_cat, f"{str(i).zfill(4)}.jpg")
            new_path = os.path.join(path_to_another_dir,
                                    f"{class_name}_{str(i).zfill(4)}.jpg")

            if os.path.isfile(path):
                shutil.copyfile(path, new_path)

                with open(csv_path, "a", newline="", encoding="utf8") as f:
                    copy_to_file = csv.DictWriter(
                        f, fieldnames=field_names, delimiter=";")

                    copy_to_file.writerow({"The Absolute Way": new_path,
                                           "Relative Way": os.path.relpath(new_path),
                                           "Class": class_name})

        class_name = "dog"
        path_to_dog = os.path.join(path_to_dataset, class_name)
        num_files = len([f for f in os.listdir(path_to_dog)
                        if os.path.isfile(os.path.join(path_to_dog, f))])

        for i in tqdm(range(0, num_files)):
            path = os.path.join(path_to_dog, f"{str(i).zfill(4)}.jpg")
            new_path = os.path.join(path_to_another_dir,
                                    f"{class_name}_{str(i).zfill(4)}.jpg")

            if os.path.isfile(path):
                shutil.copyfile(path, new_path)

                with open(csv_path, "a", newline="", encoding="utf8") as f:
                    copy_to_file = csv.DictWriter(
                        f, fieldnames=field_names, delimiter=";")

                    copy_to_file.writerow({"The Absolute Way": new_path,
                                           "Relative Way": os.path.relpath(new_path),
                                           "Class": class_name})

    else:
        if not os.path.exists(path_to_another_dir):
            os.mkdir(path_to_another_dir)

        field_names = ["The Absolute Way", "Relative Way", "Class"]
        with open(os.path.join(path_to_another_dir, "_dataset_another_dir.csv"), "w", newline="", encoding="utf8") as f:
            printer = csv.DictWriter(
                f, fieldnames=field_names, delimiter=";")
            printer.writeheader()

        class_name = "cat"
        path_to_cat = os.path.join(path_to_dataset, class_name)
        num_files = len([f for f in os.listdir(path_to_cat)
                        if os.path.isfile(os.path.join(path_to_cat, f))])

        for i in tqdm(range(0, num_files)):
            path = os.path.join(path_to_cat, f"{str(i).zfill(4)}.jpg")
            new_path = os.path.join(path_to_another_dir,
                                    f"{class_name}_{str(i).zfill(4)}.jpg")

            if os.path.isfile(path):
                shutil.copyfile(path, new_path)

                with open(os.path.join(path_to_another_dir, "_dataset_another_dir.csv"), "a", newline="", encoding="utf8") as f:
                    copy_to_file = csv.DictWriter(
                        f, fieldnames=field_names, delimiter=";")

                    copy_to_file.writerow({"The Absolute Way": new_path,
                                           "Relative Way": os.path.relpath(new_path),
                                           "Class": class_name})

        class_name = "dog"
        path_to_dog = os.path.join(path_to_dataset, class_name)
        num_files = len([f for f in os.listdir(path_to_dog)
                        if os.path.isfile(os.path.join(path_to_dog, f))])

        for i in tqdm(range(0, num_files)):
            path = os.path.join(path_to_dog, f"{str(i).zfill(4)}.jpg")
            new_path = os.path.join(path_to_another_dir,
                                    f"{class_name}_{str(i).zfill(4)}.jpg")

            if os.path.isfile(path):
                shutil.copyfile(path, new_path)

                with open(os.path.join(path_to_another_dir, "_dataset_another_dir.csv"), "a", newline="", encoding="utf8") as f:
                    copy_to_file = csv.DictWriter(
                        f, fieldnames=field_names, delimiter=";")

                    copy_to_file.writerow({"The Absolute Way": new_path,
                                           "Relative Way": os.path.relpath(new_path),
                                           "Class": class_name})
                   
        return os.path.join(path_to_another_dir, "_dataset_another_dir.csv")


def main():
    """Main function"""
    path_to_another_dir = "C:/Users/User/nuck figgers/dataset_another"
    path_to_dataset = "C:/Users/User/nuck figgers/dataset"
    csv_path = "dataset_another_dir.csv"
    copying_images_to_another(path_to_another_dir, path_to_dataset, csv_path)


if __name__ == "__main__":
    main()
