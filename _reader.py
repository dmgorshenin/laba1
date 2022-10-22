import csv
import os
import time

from tqdm import tqdm


class Iterator:
    def __init__(self, path_to_file: str, class_name: str) -> None:
        if __name__ == "__main__":
            self.class_name = class_name
            self.path_to_file = path_to_file
            self.list = []
            self.counter = 0

            if os.path.exists(self.path_to_file):
                with open(self.path_to_file, "r", encoding="utf8") as file:
                    read = csv.DictReader(
                        file, fieldnames=["The Absolute Way", "Relative Way", "Class"], delimiter=";")

                    for row in read:
                        if row["Class"] == self.class_name:
                            self.list.append(
                                [row["The Absolute Way"], row["Relative Way"], row["Class"]])

            else:
                raise FileNotFoundError

    def __iter__(self):
        if __name__ == "__main__":
            return self

    def __next__(self) -> str:
        """The function of switching to the next instance of the list in the class object

        Raises:
            StopIteration: If the counter reaches the border of the list, it throws an exception and stops the iterator

        Returns:
            str: The path to the picture 
        """
        if __name__ == "__main__":
            if self.counter < len(self.list):
                self.counter += 1
                return self.list[self.counter][0]

            elif self.counter == len(self.list):
                raise StopIteration


def main() -> None:
    path_to_file="C:/Users/User/nuck figgers/dataset.csv"
    path_to_another_dir="C:/Users/User/nuck figgers/dataset_another_dir.csv"
    path_to_random="C:/Users/User/nuck figgers/dataset_random_dir.csv"
    class_name_cat="cat"
    class_name_dog="dog"
    a=Iterator(path_to_random, class_name_dog)
    
    try:
        for i in a:
            print(i)
    except:
        pass
        


if __name__ == "__main__":
    main()
