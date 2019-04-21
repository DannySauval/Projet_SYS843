import sys

dataPath = './training/'
annotationFilePath = 'annotations.txt'
trainData = "./trainData/"
testData = "./testData/"

found_bg = False
all_imgs = {}

classes_count = {}

class_mapping = {}

visualise = True

i = 1
nbCar = 0
nbBicycle = 0
nbCarSet = 0
nbBicSet = 0

trainAn = open('trainAnnotations.txt', 'w+')
testAn = open('testAnnotations.txt', 'w+')

with open(annotationFilePath, 'r') as f:
    print('Parsing annotation files')

    for line in f:
        # Print process
        sys.stdout.write('\r' + 'idx=' + str(i))

        line_split = line.strip().split(',')

        (filename, x1, y1, x2, y2, class_name) = line_split
        filename = dataPath + filename

        if class_name == 'car':
            nbCar += 1
            if nbCarSet < 8:
                trainAn.write(line)
                nbCarSet += 1
            elif nbCarSet >= 8 and nbCarSet < 10:
                testAn.write(line)
                nbCarSet += 1
            else:
                nbCarSet = 0
        elif class_name == 'bicycle':
            nbBicycle += 1
            if nbBicSet < 8:
                trainAn.write(line)
                nbBicSet += 1
            elif nbBicSet >= 8 and nbBicSet < 10:
                testAn.write(line)
                nbBicSet += 1
            else:
                nbBicSet = 0

print()
print(nbCar)
print(nbBicycle)