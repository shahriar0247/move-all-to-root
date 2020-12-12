import os

def listall(list_path):
    all_folders = []
    all_files = []
    for root,folders,files in os.walk(list_path):
    

        for eachfile in files:
            all_files.append(os.path.join(root,eachfile))
    
    return all_files

all_files = listall(".")

for file in all_files:
    os.system("copy \"" + file + "\" .")