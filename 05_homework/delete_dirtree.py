from pathlib import Path


def delete_dirtree(root_path):
    """
    刪除指定目錄及其所有內容
    Args:
        root_path: 要刪除的目錄路徑 (Path object)
    """
    if not root_path.exists():
        print(f"路徑不存在: {root_path}")
        return
    
    if not root_path.is_dir():
        print(f"不是目錄: {root_path}")
        return
    
    # 收集所有檔案和目錄
    files = []
    dirs = []
    
    # 使用 rglob('*') 遞歸地查找所有文件和目錄
    for item in root_path.rglob('*'):  # '*' 匹配所有文件和目錄
        if item.is_file():  # 檢查是否為文件
            print(f"找到文件: {item}")
            files.append(item)
        elif item.is_dir():  # 檢查是不是資料夾
            print(f"找到資料夾: {item}")
            dirs.append(item)
    
    # 先刪除所有檔案
    for file in files:
        try:
            file.unlink()
            print(f"檔案 {file} 已被刪除。")
        except Exception as e:
            print(f"刪除檔案 {file} 失敗: {e}")
    
    # 按深度排序目錄，從最深的開始刪除（這樣可以確保先刪除子目錄）
    dirs.sort(key=lambda x: len(x.parts), reverse=True)
    
    # 刪除所有目錄
    for folder in dirs:
        try:
            if folder.exists():  # 確認目錄仍然存在
                folder.rmdir()
                print(f"資料夾 {folder} 已被刪除。")
        except Exception as e:
            print(f"刪除資料夾 {folder} 失敗: {e}")
    
    # 最後刪除根目錄
    try:
        if root_path.exists():
            root_path.rmdir()
            print(f"根目錄 {root_path} 已被刪除。")
    except Exception as e:
        print(f"刪除根目錄 {root_path} 失敗: {e}")


if __name__ == "__main__":
    # 測試用的路徑
    test_path = Path.cwd() / "dirtree"
    delete_dirtree(test_path)
