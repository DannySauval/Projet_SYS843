from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

import sys
from matplotlib import pyplot as plt
from skimage import io
import cv2

def get_data(input_path):
    found_bg = False
    all_imgs = {}

    classes_count = {}

    class_mapping = {}

    with open(input_path, 'r') as f:
        print('Parsing annotation files')

        for line in f:
            sys.stdout.write('\r' + 'idx=' + str(i))

            line_split = line.strip().split(',')

            (filename, x1, y1, x2, y2, class_name) = line_split
            filename = "./training/" + filename

            if class_name not in classes_count:
                classes_count[class_name] = 1
            else:
                classes_count[class_name] += 1

            if class_name not in class_mapping:
                if class_name == 'bg' and found_bg == False:
                    print(
                        'Found class name with special name bg. Will be treated as a background region (this is usually for hard negative mining).')
                    found_bg = True
                class_mapping[class_name] = len(class_mapping)

            if filename not in all_imgs:
                all_imgs[filename] = {}

                print(filename)

                img = cv2.imread(filename)
                (rows, cols) = img.shape[:2]
                all_imgs[filename]['filepath'] = filename
                all_imgs[filename]['width'] = cols
                all_imgs[filename]['height'] = rows
                all_imgs[filename]['bboxes'] = []

            all_imgs[filename]['bboxes'].append(
                {'class': class_name, 'x1': int(x1), 'x2': int(x2), 'y1': int(y1), 'y2': int(y2)})

        all_data = []
        for key in all_imgs:
            all_data.append(all_imgs[key])

        if found_bg:
            if class_mapping['bg'] != len(class_mapping) - 1:
                key_to_switch = [key for key in class_mapping.keys() if class_mapping[key] == len(class_mapping) - 1][0]
                val_to_switch = class_mapping['bg']
                class_mapping['bg'] = len(class_mapping) - 1
                class_mapping[key_to_switch] = val_to_switch

        return all_data, classes_count, class_mapping

while 1:
    train_imgs, classes_count, class_mapping = get_data('annotations.txt')
    print(train_imgs)
    print()
    print(classes_count)
    print()
    print(train_imgs[0]['filepath'])

    filepath = "./training/" + train_imgs[0]['filepath']

    print(filepath)

    img = io.imread(train_imgs[0]['filepath'])

    print(train_imgs[0]['bboxes'][0]['x1'])

    img_bbox = img.copy()
    for boxes in train_imgs[0]['bboxes']:
        xmin = boxes['x1']
        ymin = boxes['y1']
        xmax = boxes['x2']
        ymax = boxes['y2']
        class_name = boxes['class']
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.rectangle(img_bbox, (xmin, ymin), (xmax, ymax), (0, 255, 0), 2)
        cv2.putText(img_bbox, class_name, (xmin, ymin - 10), font, 0.5, (0, 255, 0), 2)

    height, width, _ = img.shape
    print(img.shape)
    plt.figure(figsize=(15, 10))
    plt.subplot(1, 2, 1)
    plt.title('Original Image')
    plt.imshow(img)
    plt.subplot(1, 2, 2)
    plt.title('Bboxes Image')
    plt.imshow(img_bbox)
    plt.show()