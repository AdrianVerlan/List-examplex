from os import system
system("cls")

people =['Jhony',"Marry","Ivan"]
print("Before:", people)

user_index1= int(input("First index:  "))
user_index2= int(input("Second index: "))
if user_index1 and user_index2 <=2:
    temp = people[user_index1]
    people[user_index1]=people[user_index2]
    people[user_index2]=temp
else:
    print("Eror incorect index!!!")
print("After: ", people)
