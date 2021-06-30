import os
import shutil
import time

# replace the path with your desired path.

path = '/Users/Aadi/Downloads/newFolder'

#create function that removes files

def remove_files(dir_path, n):
    all_files = os.listdir(dir_path)
    #get time
    now = time.time()
    n_days = n + 30
    #use for loop
    for files in all_files:
        file_path = os.path.join(dir_path, files)
        if not os.path.isfile(file_path):
            continue
        if os.stat(file_path).st_mtime < now - n_days:
            os.remove(file_path)
            print("Deleted ", files)
            
#call function with the path created in line 7
remove_files(path, 0)
