import difflib
import sys

filename = "review.diff"
if (len(sys.argv) <= 2):
    print("filepath1: ")
    text1 = open(input(), "r").readlines()
    print("filepath2: ")
    text2 = open(input(), "r").readlines()

else:
    text1 = open(sys.argv[1], "r").readlines()
    text2 = open(sys.argv[2], "r").readlines()
if (len(sys.argv) > 3):
    filename = sys.argv[2]+".diff"

with open (filename, "w+") as f:
    for line in difflib.unified_diff(text1, text2):
        print(line, end=' ')
        f.write(line)
