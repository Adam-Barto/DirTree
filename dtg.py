from pathlib import Path
import os


def directory_tree_generator(target_directory='test'):
    p = Path(target_directory)
    [print(file) for file in p.iterdir() if file.is_file()]
    directory_list = [str(file) for file in p.iterdir() if file.is_dir()]
    [print(file) for file in directory_list]
    if len(directory_list) != 0:
        directory_tree_generator(*directory_list)


if __name__ == '__main__':
    directory_tree_generator()
