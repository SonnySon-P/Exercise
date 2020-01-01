N = int(input("請輸入正整數N？"))
M = int(input("請輸入正整數M？"))
Count = 0
while N <= M:
    N = N ** 3
    Count = Count + 1
print(Count)