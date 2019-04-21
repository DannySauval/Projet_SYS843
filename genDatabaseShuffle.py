import random
with open('annotations.txt','r') as source:
    data = [ (random.random(), line) for line in source ]
data.sort()
with open('annotationsShuffled.txt','w+') as target:
    for _, line in data:
        target.write( line )