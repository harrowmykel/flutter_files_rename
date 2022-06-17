import os, fnmatch
from pathlib import Path
import shutil
import sys

relative_or_absolute_path_to_file = '.'

#find and replace strings in folder and subfolder
#findReplace("some_dir", "find this", "replace with this", "*.txt")
#https://stackoverflow.com/questions/4205854/python-way-to-recursively-find-and-replace-string-in-text-files
def findReplaceAllWords(directory):
    for path, dirs, files in os.walk(os.path.abspath(directory)):

        for filename in fnmatch.filter(files, "*.dart"):
            filepath = os.path.join(path, filename)
            with open(filepath) as f:
                s = f.read()

            newfilename = filename.replace('-', '_')
            newfilename.lower()

            findReplaceFileName(directory, filename, newfilename)
            os.unlink(filepath)

            newfilepath =  os.path.join(path, newfilename)

            # s = s.replace(find, replace)
            with open(newfilepath, "a+") as f:
                f.write(s)


def findReplaceFileName(directory, what, withi):
    for path, dirs, files in os.walk(os.path.abspath(directory)):

        for filename in fnmatch.filter(files, "*.dart"):
            filepath = os.path.join(path, filename)
            with open(filepath) as f:
                s = f.read()

            s = s.replace(what, withi)

            # s = s.replace(find, replace)
            with open(filepath, "w") as f:
                f.write(s)

findReplaceAllWords(relative_or_absolute_path_to_file)
