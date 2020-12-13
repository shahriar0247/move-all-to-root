import os
import subprocess
import threading
from sys import platform

def listall(list_path):
    all_folders = []
    all_files = []
    for root,folders,files in os.walk(list_path):
    

        for eachfile in files:
            all_files.append(os.path.join(root,eachfile))
    
    return all_files

def execute(cmd):
    subprocess.Popen(cmd, stdout=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)

all_files = listall(".")

number_of_files = len(all_files)
file_num = 0

for file in all_files:
    file_num = file_num + 1
    print(str(int(file_num*100/number_of_files)) + "%")
    if platform == "win32":
        cmd = ("move \"" + file + "\" .")
    else:
        cmd = ("mv \"" + file + "\" .")
    execute(cmd)
    #threading.Thread(target=execute,args=[cmd]).start()