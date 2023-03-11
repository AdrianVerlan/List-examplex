from os import system

system('cls')

rating= [ 5, 3, 4 , 2, 2, 4, 5, 1]
print("USERNAME|---|RATING")
for i in range(len(rating)):
    print("User", i+1,"=", rating[i], end=" ")
    for r in range(rating[i]):
        print("*", end="")

    print()