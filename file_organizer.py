# File organizer


""" Input data:
        - Path to folder

Const:
    - DIR_TYPES
    - FILE EXTENSION


Output:
    - Move the files in the specific folder
"""
import os
import shutil

def menu():
    path = input('Insert the path or press <Enter> to exit the program: ')
    while not path_validation(path):
            if path == '':
                exit()
            path = input('Insert the path or press <Enter> to exit the program: ')
    print('The path is valid')
    return path

"""the next function will create the folders where to store the data
    if it does not already exist"""
def create_dirs(path: str):
    for dir in DIR_TYPES:
        if not os.path.isdir(path + '\\' + dir):
            os.mkdir(path + '\\' + dir)

"""if the inserted path is a folder it will return true otherwise false"""
def path_validation(path: str) -> bool:
    return os.path.isdir(path)


"""next function extracts each file from the path we enter and returns a list"""
def list_all_files(path: str) -> list:
    files = [file for file in os.listdir(path) if os.path.isfile(path + '\\' + file)]
    return files

"""the next function will look for the last point in the file name and will only return its extension"""
def extract_file_extension(file: str) -> str:
    indexes = [i for i, ch in enumerate(file) if ch == '.']
    if indexes:
        file_extension = file[indexes[-1]::]
        return file_extension
    else:
        return 'No extension'

def map_extension_to_folder(path: str) -> dict:
    extension_mapping = {path + '\\' + dir:FILE_EXT_TYPES[i] for i,dir in enumerate(DIR_TYPES)}
    return extension_mapping
"""for each directory in DIR_TYPES (list)
I will have the key consisting of path + directory name and the value consists of FILE_EXT_TYPES"""


if __name__ == '__main__':
    DIR_TYPES = ['Pictures', 'Videos', 'PDF_files',
                 'Music', 'TXT_files', 'Python_files',
                 'Word_files', 'Excel_files', 'Exe_files',
                 'Archived_files', 'CDR_files'
                 ]

    FILE_EXT_TYPES = [['.jpg', '.jpeg', '.png', '.JPG'], ['.mp4', '.mov', '.MOV', '.avi'],
                      ['.pdf', '.PDF'], '.mp3', '.txt', '.py',
                      ['.doc', '.docx'], ['.csv', '.xlsx', '.xls'], '.exe',
                      ['.7z', '.zip'], '.cdr']


path = menu()
mapping = map_extension_to_folder(path)
create_dirs(path)
files = list_all_files(path)

"""I will extract the extension, and depending on this I will move them to the specific folder"""

for file in files:
    file_extension = extract_file_extension(file)
    for k, v in mapping.items():
        if file_extension in v:
            try:
                shutil.move(path + '\\' + file, k)
            except:
                print(file + 'cannot be moved.')











