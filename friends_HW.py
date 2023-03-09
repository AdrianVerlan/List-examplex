from os import system

system('cls')

friends =[]

while len(friends)<100:
    name= input("Add friend name: ")
    if name =="":
        break
    if name in friends:
         pass
    else:
            friends.append(name)
print("You have",len(friends, ),"friends")
for i in range(len(friends)):
    print("  ", i,">>",friends[i])

   