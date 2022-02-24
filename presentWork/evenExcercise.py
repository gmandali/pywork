num1, num2 = input().split()
numList = []
newnum1 = int(num1)
newnum2 = int(num2)
for i in range(newnum1, newnum2 + 1):
    if i % 2 == 0:
        numList.append(i)

print(*numList)
