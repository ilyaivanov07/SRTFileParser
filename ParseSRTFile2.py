# Author: Ilya Ivanov
# Date created: 01/12/2016
# The program parses .srt files in the provided directory and outputs one text file without a time stamp.
# Original .srt files are not modified

import os.path
import re
import sys

# Command line options:
# python <file_name> <input directory> <output file name>

if len(sys.argv) <= 2:
    print "Command line options:"
    print "<input directory> <output file name>"
    exit(0)

directory = sys.argv[1]
newFileName = sys.argv[2]

if not os.path.isdir(directory):
    print directory + " is not a directory"
    exit(0)

# remove time stamp that looks like 0:00:47.690
exp = re.compile("\d+:\d+:\d+.\d+")

files = os.listdir(directory) # get array of file names

# create/open a new file
newFile = open(os.path.join(directory, newFileName), "w")

for any_file in files:
    # print os.path.join(directory, filename)
    print any_file
    fullPath = os.path.join(directory, any_file)
    # print fullPath
    filename, file_extension = os.path.splitext(fullPath)

    if os.path.isfile(fullPath) and file_extension == ".srt":
        srtFile = open(fullPath, "r")
        # write file name without extension
        newFile.write("\n ------------- " + any_file.split('.')[0] + " --------------------- \n\n")

        for line in srtFile:
            if not exp.match(line):
                newFile.write(line)
        # Close file
        srtFile.close()

newFile.close()


