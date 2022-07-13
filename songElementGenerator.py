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

# Randomize order data is in
random.shuffle(data1)

random.shuffle(data2)

random.shuffle(data3)

# Create log for order of generated part ideas
with open('generatedParts.txt', 'w', encoding='utf-8') as f:
    for x in data1:
        f.write(str(x)+"\n")
        f.close

# Create log for order of generated part tips
with open('generatedTips.txt', 'w', encoding='utf-8') as f:
    for x in data2:
        f.write(str(x)+"\n")
        f.close

# Create log for order of generated part lines
with open('generatedLines.txt', 'w', encoding='utf-8') as f:
    for x in data3:
        f.write(str(x)+"\n")
        f.close



# Visually indicate output starts here
print("\n"+"\n"+"\n"+ "----------------------------------------------------------------------------------------------"
+"--------------------------------------------------------------------------"+
"\n"+"----------------------------------------------------------------------------------------------"
"--------------------------------------------------------------------------"+"\n"+"\n"+"\n")

# Get unique list of tips
topics = []
uniqueTips = []
for x in data2:
    topics.append(x.get("Topic"))
    uniqueTopics = list(set(topics))

for x in data2:
    for y in uniqueTopics:
        if x.get("Topic") == y:
            uniqueTips.append(str(x.get("Topic")+" | "+ x.get("Tip")))
            uniqueTopics.remove(y)
            break

random.shuffle(uniqueTips)

# Print random tips
for x in uniqueTips:
    print(x+"\n")

print("\n")

# Print random parts
print(data1[:5])
print("\n")

# Print random lines
print(data3[:5])