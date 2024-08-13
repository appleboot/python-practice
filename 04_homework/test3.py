def is_valid_id(id_number):
    # 檢查長度是否為10個字符
    if len(id_number) != 10:
        return False
    
    # 定義字母對應的數字
    letters = {
        'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16, 'H': 17, 'I': 34, 'J': 18,
        'K': 19, 'L': 20, 'M': 21, 'N': 22, 'O': 35, 'P': 23, 'Q': 24, 'R': 25, 'S': 26, 'T': 27,
        'U': 28, 'V': 29, 'W': 32, 'X': 30, 'Y': 31, 'Z': 33
    }
    
    # 檢查第一個字符是否為英文字母
    if id_number[0] not in letters:
        return False
    
    # 檢查剩下的9個字符是否為數字
    if not id_number[1:].isdigit():
        return False
    
    # 將字母轉換為數字
    n1 = letters[id_number[0]]
    n2 = int(id_number[1])
    n3 = int(id_number[2])
    n4 = int(id_number[3])
    n5 = int(id_number[4])
    n6 = int(id_number[5])
    n7 = int(id_number[6])
    n8 = int(id_number[7])
    n9 = int(id_number[8])
    n10 = int(id_number[9])
    # 計算檢查碼
    checksum = (n1 // 10) + (n1 % 10) * 9 + n2 * 8 + n3 * 7 + n4 * 6 + n5 * 5 + n6 * 4 + n7 * 3 + n8 * 2 + n9 + n10
    print(n1 % 10)
    # 檢查是否能被10整除
    return checksum % 10 == 0
    
# 測試範例
is_valid_id("A123456789")
is_valid_id("T124044878")
