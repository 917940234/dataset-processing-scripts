import os
import re
import shutil
import tempfile


def rename_and_move_files(directory):
    suffix = ".png"
    prefix_counter = {}
    for root, _, files in os.walk(directory):
        for file in files:
            match = re.match(r'([a-zA-Z_]+)(\d+)', file)
            if match:
                prefix, number = match.groups()
                if prefix not in prefix_counter:
                    prefix_counter[prefix] = 1
                else:
                    prefix_counter[prefix] += 1

                old_file_path = os.path.join(root, file)
                new_file_name = f"{prefix}{prefix_counter[prefix]}{suffix}"
                new_file_path = os.path.join(root, new_file_name)

                with tempfile.TemporaryDirectory() as temp_dir:
                    temp_file_path = os.path.join(temp_dir, file)
                    shutil.copy(old_file_path, temp_file_path)
                    shutil.move(temp_file_path, new_file_path)

                new_folder = os.path.join(directory, prefix)
                if not os.path.exists(new_folder):
                    os.makedirs(new_folder)

                shutil.move(new_file_path, os.path.join(new_folder, new_file_name))
                print(f"Renamed '{file}' to '{new_file_name}', moved to '{new_folder}'")


if __name__ == "__main__":
    directory = r"C:\Users\91794\Documents\SyncSpace\IdeaStorm\PycharmProjects\ScrapMind\dataset\images"
    rename_and_move_files(directory)
