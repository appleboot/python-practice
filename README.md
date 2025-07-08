# Python Practice Repository

這是一個Python練習題庫，包含各種編程練習和作業。

## 目錄結構

### 01_fizzbuzz/
- **main.py**: FizzBuzz遊戲的實作
  - 當數字被3整除時印出"fizz"
  - 當數字被5整除時印出"buzz"  
  - 當數字被7整除時印出"jazz"
  - 組合情況會印出組合字串（如fizzbuzz, fizzjazz等）

### 02_pyramid/
- **main.py**: 印出星號組成的金字塔圖案
- **test.py**: 相關測試檔案

### 03_test/
- **check.py**: 簡單的條件判斷練習
- **test11.py**: 資料處理練習 - 找出最高分數和最輕體重的人

### 04_homework/
包含六個不同的練習題：
- **test1.py**: 階乘計算（遞迴實作）
- **test2.py**: 回文字串檢查器
- **test3.py**: 台灣身分證號碼驗證器
- **test4.py**: Connect 6 遊戲（tkinter GUI實作）
- **test5.py**: 計算1到100,000,000的總和
- **test6.py**: 另一種回文檢查實作

### 05_homework/
目錄樹管理系統：
- **random_dirtree.py**: 建立隨機的目錄結構和檔案
- **delete_dirtree.py**: 遞迴刪除整個目錄樹
- **main.py**: 主程式 - 建立測試目錄然後刪除

## 如何使用

每個目錄都可以獨立執行，例如：

```bash
# 執行FizzBuzz
python 01_fizzbuzz/main.py

# 執行金字塔程式
python 02_pyramid/main.py

# 測試目錄樹管理
python 05_homework/main.py

# 執行個別練習題
python 04_homework/test1.py
python 04_homework/test2.py
# ... 等等
```

## 練習內容

這個練習庫涵蓋了以下Python概念：
- 基本語法和控制結構
- 遞迴函數
- 字串處理
- 檔案和目錄操作
- GUI程式設計（tkinter）
- 資料結構操作
- 演算法實作

## 注意事項

- 所有程式都是使用Python 3編寫
- 部分程式需要輸入參數或使用者互動
- GUI程式（test4.py）需要支援tkinter的環境

---

**這邊可以幹嘛？**

這個練習庫可以用來：
1. 學習Python基礎程式設計
2. 練習常見的演算法問題
3. 了解檔案系統操作
4. 體驗GUI程式開發
5. 作為程式設計教學的範例