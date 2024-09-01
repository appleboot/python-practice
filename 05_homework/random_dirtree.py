from random import randint
from pathlib import Path


def make_random_dirtree(root: Path, depth: int, max_depth: int = 3):
    file_count = randint(1, 10)
    for i in range(file_count):
        file_name = f"text{i}.txt"
        file_path = root / file_name
        file_path.write_text(f"Hello, world! from {file_name}")

    if depth >= max_depth:
        return

    dir_count = randint(1, 5)

    for i in range(dir_count):
        dir_name = f"dir{i}"
        dir_path = root / dir_name
        dir_path.mkdir()
        make_random_dirtree(dir_path, depth=depth + 1, max_depth=max_depth)
留言
建議修訂
delete_dirtree.py
from pathlib import Path


def delete_dirtree(root):
    ...