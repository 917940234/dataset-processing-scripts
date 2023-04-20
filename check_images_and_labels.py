# 该脚本用于检查images和labels文件夹下是否存在同名的图片和标签文件
# 并且判断哪些图片没有对应的标签文件
import os
import glob

img_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.jfif', '.webp')
img_folder = 'C:\SyncSpace\IdeaStorm\PycharmProjects\datasets\scrap\lightclose\images'
label_folder = 'C:\SyncSpace\IdeaStorm\PycharmProjects\datasets\scrap\lightclose\labels'

# 查找images文件夹下的所有图片文件
img_files = [f for f in glob.glob(os.path.join(img_folder, '*')) if f.lower().endswith(img_extensions)]

# 遍历每个图片文件，查找是否有对应的标签文件
for img_file in img_files:
    # 获取图片文件名和扩展名
    img_filename, img_ext = os.path.splitext(os.path.basename(img_file))
    # 构造标签文件路径
    label_file = os.path.join(label_folder, img_filename + '.txt')
    # 如果标签文件不存在，打印提示信息
    if not os.path.exists(label_file):
        print(f"No label file for image '{img_file}'")
