import os
import shutil

from_dir="C:/Users/User/Downloads"
to_dir="C:/Users/User/Documents/Document_Files"

list_of_files=os.listdir(from_dir)
#print(list_of_files)

for file_name in list_of_files:
    name,ext=os.path.splitext(file_name)
    
    if ext=="":
        continue
    if ext in [".gif", ".png", ".jpg", ".jpeg", ".jfif"]:
        path1=from_dir+"/"+file_name
        path2=to_dir+"/"+file_name
        print("path1:", path1)
        print("path2:", path2)
        if os.path.exists(path2): print("Moving " + file_name + ".....")