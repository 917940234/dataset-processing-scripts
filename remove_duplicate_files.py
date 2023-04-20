import os
import hashlib

def remove_duplicates(directory):
    file_hashes = set()
    files = os.listdir(directory)

    for file in files:
        file_path = os.path.join(directory, file)

        if os.path.isfile(file_path):
            with open(file_path, 'rb') as f:
                file_hash = hashlib.md5(f.read()).hexdigest()

            if file_hash in file_hashes:
                os.remove(file_path)
                print(f"Removed duplicate file: {file_path}")
            else:
                file_hashes.add(file_hash)

if __name__ == "__main__":
    directory = r"C:\Users\91794\Documents\SyncSpace\Projects\5. 废钢物料识别\image"
    remove_duplicates(directory)
