import platform
import os
import pathlib

file_path = os.path.abspath(__file__) # full path of your script
dir_path = os.path.dirname(file_path) # full path of the directory of your script
script_path = os.path.join(dir_path,'lsym.py')

if platform.system().lower() == "linux":
    os.system("alias lsym='python3 {}'".format(script_path))
    os.system("touch ~/.bash_aliases")
    path = pathlib.Path.home()
    path = os.path.join(path, ".bash_aliases")
    try:
        with open(path, 'a') as file:
            file.write("alias lsym='python3 {}'".format(script_path))
    except Exception as e:
        print("LSYM INSTALLATION ERROR:", e)

elif platform.system().lower() == "windows":
    print("Sorry, windows installation is underway")

print("Done!")
