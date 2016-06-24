#!/usr/bin/env python

# @author Garrett Gutierrez
# @date 23 June 2016
# This program appends a timestamp to a file.
# python CHKDDL.py <filename>

# import python libraries
import sys, datetime

# Global variables
# Number of arguments including file name
NUMBER_OF_ARGUMENTS = 2

# @param fileName The name of the file to have a timestamp appended.
def appendTimestampToFile(fileName):
    try:
        file = open(fileName, 'a')
        file.write("-- " + fileName + " updated at " + '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()))
        file.write("\n")
    except:
        print(sys.argv[0] + " error: " + fileName + " could not be opened.")
        exit(-1)

# Driver of the program
def main():
    if (len(sys.argv) == NUMBER_OF_ARGUMENTS):
        appendTimestampToFile(sys.argv[1])
    else:
        print(sys.argv[0] + " error: Incorrect number of arguments.\nExpected: " + str(NUMBER_OF_ARGUMENTS))

# Check namespace and run main
if __name__ == '__main__':
    main()
