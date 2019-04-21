import os
import sys

from shutil import copyfile

annotationFilePath = 'testAnnotationsShuffled.txt'
dataPath = './training/'
destPath = './testData/'

#trainAn = open('trainAnnotations.txt', 'w+')
testAn = open('testAnnotationsFinal.txt', 'w+')

with open(annotationFilePath, 'r') as f:
    print('Parsing annotation files')

    for line in f:
        line_split = line.strip().split(',')
        print(line)
        (filename, x1, y1, x2, y2, class_name) = line_split

        filename2 = dataPath + filename

        dest = destPath + filename
        copyfile(filename2, dest)

        testAn.write(line)
