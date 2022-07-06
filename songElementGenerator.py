# importing the module
from enum import unique
import json
import sys
import random
from token import NEWLINE


# open the file in read mode
with open("parts.json", encoding='utf-8') as d1:
    data1 = json.load(d1)
    d1.close

with open("tips.json", encoding='utf-8') as d2:
    data2 = json.load(d2)
    d2.close    

with open("lines.json", encoding='utf-8') as d3:
    data3 = json.load(d3)
    d3.close  

random.shuffle(data1)

random.shuffle(data2)

random.shuffle(data3)

with open('generatedParts.txt', 'w', encoding='utf-8') as f:
    for x in data1:
        f.write(str(x)+"\n")
        f.close

with open('generatedTips.txt', 'w', encoding='utf-8') as f:
    for x in data2:
        f.write(str(x)+"\n")
        f.close

with open('generatedLines.txt', 'w', encoding='utf-8') as f:
    for x in data3:
        f.write(str(x)+"\n")
        f.close




print("\n"+ "--------------------------------------------------------------------------"
+"--------------------------------------------------------------------------"+
"\n"+"--------------------------------------------------------------------------"
"--------------------------------------------------------------------------"+"\n")


topics = []

for x in data2:
    topics.append(x.get("Topic"))
    uniqueTopics = list(set(topics))

random.shuffle(uniqueTopics)

for x in data2:
    for y in uniqueTopics:
        if x.get("Topic") == y:
            print(x.get("Tip"))
            print("\n")
            uniqueTopics.remove(y)
            break
print("\n")

print(data1[:5])
print("\n")

print(data3[:5])