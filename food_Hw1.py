from os import system
system('cls')

o_food_name  = ["Pizza", "Salad","Soupi"]
o_food_price = [50.00, 43.7, 23.05]
o_food_q     = [ 2, 4, 8]
total = 0
for i in range(len(o_food_name)):
    print(f"",i+1,":",o_food_name[i],"|",o_food_price[i],"|",o_food_q[i])
    total += o_food_price[i] * o_food_q[i]
print()
print("Total cost:", "{:.2f}".format(total))
