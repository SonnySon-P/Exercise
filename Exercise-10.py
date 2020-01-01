Type = " "
List = []
while Type != "q":
    Number = input("請輸入號碼？")
    List.append(Number)
    Type = Number
List.remove("q")
for i in range(len(List)-1, -1, -1):
    print(List[i])