from os import system

system('cls')

friends =[]

while len(friends)<100:
    name= input("Add friend name: ")
    if name =="":
        break
    if name in friends:
         print("You already write this name")
    else:
            friends.append(name)
print()
print("You have",len(friends, ),"friends")
for i in range(len(friends)):
    print("  ", i,">>",friends[i])
print()

   