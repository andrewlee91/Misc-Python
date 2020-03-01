import os
from datetime import datetime
import random
import sys


def Check_Arguments():
    if len(sys.argv) == 1:
        print(
            "No directory argument passed. Would you like to rename files in the current directory? (Y/N)"
        )
        if input().lower() == "y":
            return os.getcwd()
        else:
            quit()
    else:
        if os.path.exists(sys.argv[1]):
            return sys.argv[1]
        else:
            print("Directory does not exist.")
            quit()


if __name__ == "__main__":
    dir_path = Check_Arguments()

    for i, j in enumerate(os.listdir(dir_path)):
        date = datetime.now().strftime("%d-%b-%y")
        time = datetime.now().strftime("%H-%M-%S")

        filename = f"{date} {time} {i}.png"

        print(f"Renaming {j} to {filename}")

        os.rename(os.path.join(dir_path, j), os.path.join(dir_path, filename))
