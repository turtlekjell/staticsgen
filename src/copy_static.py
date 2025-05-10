import os
import shutil

def copy_static_files(src_dir, dest_dir):
    # Remove old public directory if it exists
    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)
        print(f"Deleted existing directory: {dest_dir}")

    # Recreate the destination directory
    os.mkdir(dest_dir)
    print(f"Created directory: {dest_dir}")

    # Start recursive copy
    _recursive_copy(src_dir, dest_dir)


def _recursive_copy(src, dest):
    for item in os.listdir(src):
        src_path = os.path.join(src, item)
        dest_path = os.path.join(dest, item)

        if os.path.isdir(src_path):
            os.mkdir(dest_path)
            print(f"Created directory: {dest_path}")
            _recursive_copy(src_path, dest_path)
        else:
            shutil.copy(src_path, dest_path)
            print(f"Copied file: {src_path} → {dest_path}")
