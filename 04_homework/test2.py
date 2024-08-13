def is_palindrome(s):
    # 移除字串中的空白和非字母數字字符，並將字串轉為小寫
    cleaned_s = ''.join(filter(str.isalnum, s)).lower()
    # 檢查字串是否等於其反轉的版本
    return cleaned_s == cleaned_s[::-1]

# 測試範例
print(is_palindrome("abcdcba"))  # True
print(is_palindrome("上海自來水來自海上"))  # True
print(is_palindrome("hello"))  # False
