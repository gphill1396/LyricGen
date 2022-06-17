# importing the module
import json
import random
from token import NEWLINE
 
# open the file in read mode
with open('lines.json') as lines:
    data = json.load(lines)

random.shuffle(data)
with open('generatedBars.txt', 'w') as f:
    for x in data:
        f.write(str(x)+"\n")
print("Done!")
