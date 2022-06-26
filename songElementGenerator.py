# importing the module
import json
import sys
import random
from token import NEWLINE

def generateContents(fileName1, fileName2):

    # open the file in read mode
    with open(fileName1) as d1:
        data1 = json.load(d1)

    with open(fileName2) as d2:
        data2 = json.load(d2)    

    random.shuffle(data1)

    random.shuffle(data2)

    with open('generatedData1.txt', 'w') as f:
        for x in data1:
            f.write(str(x)+"\n")
    with open('generatedData2.txt', 'w') as f:
        for x in data2:
            f.write(str(x)+"\n")

    print("Done!"+"\n")
    print(data1[:5])
    print("\n")
    print(data2[:5])

if __name__ == "__main__":
    fileName1 = str(sys.argv[1])
    fileName2 = str(sys.argv[2])
    generateContents(fileName1, fileName2)
