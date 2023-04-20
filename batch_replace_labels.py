import os
import re

annotations_dir = r"C:\Users\91794\Documents\SyncSpace\IdeaStorm\PycharmProjects\ScrapMind\dataset\labels"  # 修改为您的标注文件目录

for filename in os.listdir(annotations_dir):
    if filename.endswith(".txt"):
        with open(os.path.join(annotations_dir, filename), "r+", encoding="gbk") as f:
            # 读取文件内容并替换标签
            content = f.read()
            content = re.sub(r'^9(?=\s)', '0', content, flags=re.MULTILINE)
            content = re.sub(r'^8(?=\s)', '1', content, flags=re.MULTILINE)
            f.seek(0)  # 将文件指针移动到文件开头
            f.write(content)  # 将替换后的内容写回文件
            f.truncate()  # 清空文件指针后面的内容
