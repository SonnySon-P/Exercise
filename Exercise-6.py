A = int(input("請輸入正整數A？"))
B = int(input("請輸入正整數B？"))
Str = ""
Ans = 0
for i in range(A, B+1, 1):
    if i == B:
        Str = Str + str(i) + "="
    else:
        Str = Str + str(i) + "+"
    Ans = Ans + i
print(Str + str(Ans))