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

def get_files_in_folder(directory):
    finded_files = []
    for root, dirs, files in os.walk(directory):
        for filename in files:
            path = os.path.join(root, filename)
            finded_files.append({"path": path, "name": filename, "size": get_file_size(path)})
    return finded_files

def get_duplicates():
    duplicates = []
    all_files = get_files_in_folder(check_folder())
    for i in range(len(all_files)-1):
        for j in range(i+1, len(all_files)):
            if (all_files[i]['name'] == all_files[j]['name']) and (all_files[i]['size'] == all_files[j]['size']):
                duplicates.append(
                    {'name': all_files[i]['name'], 'path': {all_files[i]['path'], all_files[j]['path']}})
    return duplicates

if __name__ == '__main__':

    print(get_duplicates())

