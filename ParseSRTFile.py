# Author: Ilya Ivanov
# Date created: 01/11/2016
# The program parses .srt files in the provided directory and outputs text files without a time stamp.
# The file names remain the same except for the extension that is changed to .txt
# Original .srt files are not modified

import os.path
import re
import sys

# Command line options:
# python <file_name> <input directory>

if len(sys.argv) <= 1:
    print "Command line options:"
    print "<input directory>"
    exit(0)

# Open a directory
directory = sys.argv[1]
if not os.path.isdir(directory):
    print directory + " is not a directory"
    exit(0)

# remove time stamp that looks like 0:00:47.690
exp = re.compile("\d+:\d+:\d+.\d+")

files = os.listdir(directory) #array of file names

for any_file in files:
    #print os.path.join(directory, filename)
    print any_file
    fullPath = os.path.join(directory, any_file)
    srtFile = open(fullPath, "r")
    #print fullPath
    filename, file_extension = os.path.splitext(fullPath)
    if os.path.isfile(fullPath) and file_extension == ".srt":
        newFile = open(os.path.join(directory, filename + ".txt"), "w")
        for line in srtFile:
            if not exp.match(line):
                newFile.write(line)
        newFile.close()

    # Close file
    srtFile.close()



