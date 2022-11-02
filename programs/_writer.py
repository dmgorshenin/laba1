import csv
import os

from tqdm import tqdm


def write_annotation(path_to_dataset: str, csv_path: str) -> None:
    """Write paths to csv file

    Args:
        class_name (str): Name of the image class
        number (int): The sequential number of the image
        csv_file (str): Name of the csvfile

    Raises:
        NotFoundErr: If the file extension is not csv , an exception is raised
    """
    if __name__ == "__main__":
        field_names = ["The Absolute Way", "Relative Way", "Class"]
        with open(csv_path, "w", newline="", encoding="utf8") as f:
            printer = csv.DictWriter(f, fieldnames=field_names, delimiter=";")
            printer.writeheader()

        class_name = "cat"
        path_to_cat = path_to_dataset + "/" + class_name
        num_files = len([f for f in os.listdir(path_to_cat)
                         if os.path.isfile(os.path.join(path_to_cat, f))])

        for i in tqdm(range(0, num_files)):
            with open(csv_path, "a", newline="", encoding="utf8") as f:
                print_in_file = csv.DictWriter(
                    f, fieldnames=field_names, delimiter=";")

                path = f"dataset/{class_name}/{str(i).zfill(4)}.jpg"

                if os.path.isfile(path):
                    print_in_file.writerow({"The Absolute Way": path_to_dataset + f"/{class_name}/{str(i).zfill(4)}.jpg",
                                            "Relative Way": f"dataset/{class_name}/{str(i).zfill(4)}.jpg",
                                            "Class": class_name})

        class_name = "dog"
        path_to_dog = path_to_dataset + "/" + class_name
        num_files = len([f for f in os.listdir(path_to_dog)
                         if os.path.isfile(os.path.join(path_to_dog, f))])

        for i in tqdm(range(0, num_files)):
            with open(csv_path, "a", newline="", encoding="utf8") as f:
                print_in_file = csv.DictWriter(
                    f, fieldnames=field_names, delimiter=";")

                path = f"dataset/{class_name}/{str(i).zfill(4)}.jpg"

                if os.path.isfile(path):
                    print_in_file.writerow({"The Absolute Way": path_to_dataset + f"/{class_name}/{str(i).zfill(4)}.jpg",
                                            "Relative Way": f"dataset/{class_name}/{str(i).zfill(4)}.jpg",
                                            "Class": class_name})


def main() -> None:
    """Main function"""
    path_to_dataset = "C:/Users/User/nuck figgers/dataset"
    csv_path="dataset.csv"
    write_annotation(path_to_dataset, csv_path)


if __name__ == "__main__":
    main()
