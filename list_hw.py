from os import system
system("cls")
L = [1, 2, 3, 4, 5]

for i in range(len(L)//2):
    temp = L[i]
    L[i] = L[-i-1]
    L[-i-1] = temp


print(L)
