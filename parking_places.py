from os import system
system("cls")

p= ["Mercedes",None,"BMW", None,None,"Toyota","BMW"]

user_car_brand =input("Car Brand ? ")
user_park_index = int(input("what place? "))
if p[user_park_index] == None:
    print("You can park!")
    p[user_park_index]= user_car_brand
else:
    print("You can't park!")
total =len(p)
free = 0
for i in range(len(p)):
    if p[i]== None:
        free+=1
print("Parking (free/total): ", free,"/",total, "places")
print()
print("Total Cars")
print("------------------------")
brands =set(p)
for b in brands:
    if b !=None:
        count= p.count(b)
        print(f"{count}:| {b}")