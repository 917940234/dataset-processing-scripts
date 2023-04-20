"""
该脚本将 YOLO 格式的标签（类别、x、y、w、h）转换为顶点坐标格式
（类别、x1、y1、x2、y2、x3、y3、x4、y4），其中 x1、y1、x2、y2、x3、y3、x4、y4 是
边界框四个角的归一化坐标。

脚本将处理指定输入目录及其子目录下的所有 .txt 文件，并将转换后的标签
保存在相应的输出目录中。

使用方法：
1. 将 'path/to/your/input_labels' 替换为输入标签目录的路径。
2. 将 'path/to/your/output_labels' 替换为输出标签目录的路径。
3. 如果您的图片尺寸不是 1920x1080，请更新 img_width 和 img_height 变量。
4. 运行脚本。

注意：
- 该脚本假设所有图像具有相同的尺寸。如果您的图像尺寸不同，您需要为每张图像提供相应的宽度和高度。
  您可以根据实际情况修改代码以适应您的需求。
  没有归一化，属于实验脚本，没有实用性
"""

import os


def yolo_to_corners(label_path, img_width, img_height):
    with open(label_path, 'r') as f:
        lines = f.readlines()

    new_labels = []
    for line in lines:
        parts = line.strip().split(' ')
        category, x, y, w, h = int(parts[0]), float(parts[1]), float(parts[2]), float(parts[3]), float(parts[4])

        x1 = (x - w / 2) * img_width
        y1 = (y - h / 2) * img_height
        x2 = (x + w / 2) * img_width
        y2 = y1
        x3 = x2
        y3 = (y + h / 2) * img_height
        x4 = x1
        y4 = y3

        new_labels.append((category, x1, y1, x2, y2, x3, y3, x4, y4))

    return new_labels


def save_new_labels(new_labels, output_path):
    with open(output_path, 'w') as f:
        for label in new_labels:
            f.write(' '.join(map(str, label)) + '\n')


label_path = 'testlabel.txt'
output_path = 'testlabel_output.txt'
img_width = 1920
img_height = 1080

new_labels = yolo_to_corners(label_path, img_width, img_height)
save_new_labels(new_labels, output_path)
