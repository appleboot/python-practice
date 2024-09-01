import shutil
from pathlib import Path
from random_dirtree import make_random_dirtree
from delete_dirtree import delete_dirtree


def main():
    root = Path(__file__).resolve().parent / "dirtree"
    shutil.rmtree(root, ignore_errors=True)
    root.mkdir(exist_ok=True)
    make_random_dirtree(root, 0, max_depth=5)
    delete_dirtree(root)


if __name__ == "__main__":
    main()