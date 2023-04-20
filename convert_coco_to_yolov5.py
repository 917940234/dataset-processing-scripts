# -*- coding: utf-8 -*-
"""
convert_coco_to_yolov5.py

This script converts a COCO dataset format annotations.json file to a set of
txt files for YOLOv5 dataset. The output format for each line starts with
a labels "0,1,2,3" corresponding to the category_id in the annotations object
in the json file. Each labels is followed by normalized coordinates based on
the width and height of the image resolution from the image_id object in the
annotations. Each image will have a corresponding txt file, including all
annotations for that image.

将'path/to/annotations.json'替换为您的COCO数据集annotations.json文件的路径，
将'path/to/output/directory'替换为您希望保存生成的YOLOv5标注文件的目录。然后运行此脚本，它将为每个图像生成对应的txt文件。
"""

import json
import os


def convert_coco_to_yolov5(annotations_file, output_dir):
    with open(annotations_file, 'r') as f:
        data = json.load(f)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    images = {}
    for image in data['images']:
        images[image['id']] = {'file_name': image['file_name'], 'width': image['width'], 'height': image['height']}

    for annotation in data['annotations']:
        category_id = annotation['category_id']
        image_id = annotation['image_id']
        image = images[image_id]

        # os.path.splitext(image['file_name'])将图像文件名（例如："image001.jpg"）分为两部分：文件名（不包括扩展名）和扩展名。
        # 这个函数返回一个包含两个元素的元组，第一个元素是文件名（不包括扩展名），第二个元素是扩展名。
        file_name = os.path.splitext(image['file_name'])[0] + '.txt'
        output_path = os.path.join(output_dir, file_name)

        # 首先，检查所有轮廓线信息是否属于相同的物体类别
        category_id = annotation.get('category_id')
        if category_id is None:
            raise ValueError('category_id is missing in the annotation')

        # 然后，遍历所有轮廓线信息并进行归一化处理
        for segmentation in annotation['segmentation']:
            normalized_coordinates = [coord / image['width'] if index % 2 == 0 else coord / image['height']
                                      for index, coord in enumerate(segmentation)]

            # 最后，将归一化后的信息写入文件中
            with open(output_path, 'a') as f:
                f.write(f"{category_id} " + " ".join(map(str, normalized_coordinates)) + "\n")

if __name__ == '__main__':
    annotations_file = r'C:\SyncSpace\IdeaStorm\PycharmProjects\datasets\scrap\lightfar\annotations.json'
    output_dir = r'C:\SyncSpace\IdeaStorm\PycharmProjects\datasets\scrap\lightfar'
    convert_coco_to_yolov5(annotations_file, output_dir)
