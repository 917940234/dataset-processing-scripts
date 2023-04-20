import os
import shutil
import tempfile
import glob
from pathlib import Path


def batch_rename_images(directory, prefix, suffix):
    img_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.jfif', '.webp')
    image_files = [f for f in glob.glob(os.path.join(directory, '*')) if f.lower().endswith(img_extensions)]

    for index, img_file in enumerate(image_files, start=1):
        file_path = Path(img_file)
        new_file_name = f"{prefix}{index}{suffix}"
        new_file_path = Path(directory) / new_file_name

        with tempfile.TemporaryDirectory() as temp_dir:
            temp_file_path = Path(temp_dir) / new_file_name  # 使用新的文件名
            shutil.copy(file_path, temp_file_path)
            shutil.move(temp_file_path, new_file_path)

        print(f"Renamed '{img_file}' to '{new_file_name}'")


# 小型废钢：small_scrap_
# 轻型废钢：light_scrap_
# 中型废钢：medium_scrap_
# 重型废钢：heavy_scrap_
# 压块废钢：compressed_scrap_
# 剪切废钢：sheared_scrap_
# 铁屑废钢：iron_filings_
# 渣钢：slag_scrap_
if __name__ == "__main__":
    root_directory = r"C:\Users\91794\Documents\SyncSpace\IdeaStorm\PycharmProjects\ScrapMind\dataset\images"  # 修改为您的图片目录
    suffix = ".png"  # 自定义后缀，例如：'.jpg'、'.png' 等

    # 遍历根目录下的所有子文件夹
    for subdir in Path(root_directory).glob('*'):
        if subdir.is_dir():
            # 使用子文件夹的名称作为前缀
            prefix = f"{subdir.name}_"
            batch_rename_images(subdir, prefix, suffix)