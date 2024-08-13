def factorial(n):
    # 基本情況：如果 n 是 0 或 1，返回 1
    if n == 0 or n == 1:
        return 1
    # 遞迴情況：n 乘以 (n-1) 的階乘
    else:
        return n * factorial(n-1)

# 測試範例
print("請輸入階乘數字:")
number = int(input())
result = factorial(number)
print(f"{number} 的階乘是 {result}")
