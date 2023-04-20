# 该脚本用于将指定目录下的所有图片随机划分为YOLO数据集的训练集和验证集
# 并将相应的标注文件复制到对应的目录中
# 训练集和验证集的比例可以通过train_ratio参数指定，默认为0.8
import os
import shutil
from sklearn.model_selection import train_test_split
import glob

# 图片和标签的根目录
data_dir = r'C:\Users\91794\Documents\SyncSpace\IdeaStorm\PycharmProjects\ScrapMind\datasets'
image_dir = os.path.join(data_dir, 'images')
label_dir = os.path.join(data_dir, 'labels')

# 创建 train 和 val 文件夹
for folder in ['train', 'val']:
    os.makedirs(os.path.join(image_dir, folder), exist_ok=True)
    os.makedirs(os.path.join(label_dir, folder), exist_ok=True)

# 获取所有图片的文件名
image_files = glob.glob(os.path.join(image_dir, '*.png'))
# 获取所有标签的文件名
label_files = glob.glob(os.path.join(label_dir, '*.txt'))

# 将图片和标签文件随机分成训练集和验证集
train_image_files, val_image_files, train_label_files, val_label_files = train_test_split(image_files, label_files, test_size=0.2, random_state=42)

# 复制训练集图片和标签到对应文件夹
for image_file, label_file in zip(train_image_files, train_label_files):
    # 复制图片
    src_image_path = image_file
    dest_image_path = os.path.join(image_dir, 'train', os.path.basename(image_file))
    shutil.copy(src_image_path, dest_image_path)
    # 复制标签
    src_label_path = label_file
    dest_label_path = os.path.join(label_dir, 'train', os.path.basename(label_file))
    shutil.copy(src_label_path, dest_label_path)

# 复制验证集图片和标签到对应文件夹
for image_file, label_file in zip(val_image_files, val_label_files):
    # 复制图片
    src_image_path = image_file
    dest_image_path = os.path.join(image_dir, 'val', os.path.basename(image_file))
    shutil.copy(src_image_path, dest_image_path)
    # 复制标签
    src_label_path = label_file
    dest_label_path = os.path.join(label_dir, 'val', os.path.basename(label_file))
    shutil.copy(src_label_path, dest_label_path)