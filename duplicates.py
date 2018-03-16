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


def get_file_size(filename):
    filesize = os.path.getsize(filename)
    return filesize

def find_duplicates(directory):
    duplicates = {}
    for dirs, subdirs, files in os.walk(directory):
        for filename in files:
            path = os.path.join(dirs, filename)
            size = get_file_size(path)
            dup = duplicates.get(size)
            if dup:
                try:
                    duplicates[size][filename].append(path)
                except KeyError:
                    duplicates[size][filename] = [path]
            else:
                duplicates[size] = {filename: [path]}
    return duplicates

if __name__ == '__main__':

    duplicates = find_duplicates(check_folder())
    for items in duplicates:
        for file in duplicates[items]:
            if len(duplicates[items][file]) > 1:
                print("Нашёл файлы с одинаковым размером и именем: {}".format(', '.join(duplicates[items][file])))

