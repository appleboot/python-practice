from pathlib import Path


def delete_dirtree():


    #先組路徑
    dir_path = Path.cwd() / "dirtree" #這邊覺得神奇 可以用/組路徑
    #先判斷路徑的檔案跟資料夾 是否同時存在
    if dir_path.exists() and dir_path.is_dir():
        # 用來存儲找到的所有檔案
        files = []
        dirs = []
        # 使用 rglob('*') 遞歸地查找所有文件
        for item in dir_path.rglob('*'):  # '*' 匹配所有文件和目錄
            if item.is_file():  # 檢查是否為文件
                print(f"找到文件: {item}")
                files.append(item)
                item.unlink()
            if item.is_dir():  # 檢查是不是資料夾
                print(f"找到資料夾: {item}")
                dirs.append(item) #這一段有點不太應處
        
        for folder in dirs:
            # 在刪除資料夾之前，確保其所有內容都已經被刪除
            if not any(folder.iterdir()):  # 如果資料夾是空的
                folder.rmdir()
                print(f"資料夾 {folder} 已被刪除。")
            
        
    #這邊我想先設計 可以找到全部資料檔
   
 
    #再由這邊設計 所有刪除檔案

    #再刪除 空白的資料夾


if __name__ == "__main__":
    delete_dirtree()  # 這裡應該傳入一個實際的路徑
