from pathlib import Path
from random_dirtree import make_random_dirtree
from delete_dirtree import delete_dirtree


def main():
    root = Path(__file__).resolve().parent / "dirtree"

    if not root.exists():
        root.mkdir(exist_ok=True)
        make_random_dirtree(root, 0, max_depth=5)

    delete_dirtree(root)

    if root.exists():
        print("Failed to delete dirtree.")
    else:
        print("Congratulations! dirtree is deleted.")


if __name__ == "__main__":
    main()