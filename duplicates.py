import sys
import os

def check_folder():
    if len(sys.argv) > 1:
        if os.path.isdir(sys.argv[1]) == True:
            folder = sys.argv[1]
            return folder
        else:
            print("Нет такой директории")    
    else:
        print("Забыл указать директорию, попробуй запустить так: python duplicates.py ~/Video/")

def get_files_in_folder(directory):
    pass

if __name__ == '__main__':
    print(check_folder())

