# Author: Ilya Ivanov
# Date created: 05/18/2016
# The program parses .srt files in the provided directory recursively and outputs one text file for each directory
# without a time stamp.
# Original .srt files are not modified

import os.path
import re
import sys


directory = "C:\Users\iivanov\Downloads\Artificial Intelligence for Robotics Subtitles"

if not os.path.isdir(directory):
    print directory + " is not a directory"
    exit(0)

# time stamp that looks like 0:00:47.690
exp = re.compile("\d+:\d+:\d+.\d+")
exp2 = re.compile("\d+")
exp3 = re.compile("{\\n\\r}")

items = os.listdir(directory)

# loop through each directory in the given directory
for item in items:
    possibleDir = os.path.join(directory, item)
    if os.path.isdir(possibleDir):
        # get files from this directory
        files = os.listdir(possibleDir)

        # loop through each file in the directory
        for any_file in files:
            filePath = os.path.join(possibleDir, any_file)
            filename, file_extension = os.path.splitext(filePath)

            if os.path.isfile(filePath) and file_extension == ".srt":
                os.remove(filePath)


# items = os.walk(directory)

# for root, dirs, files in items:
#     print dirs
#     print files

#print files



