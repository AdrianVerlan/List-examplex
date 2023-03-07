from os import system
system('cls')
students=["Studnet 1","Student 2","Student 3"]
marks =[
    [
    [5, 6, 3, 7],
    [7, 8, 5, 9],
    [9, 4, 5, 6],
    ],
    [
    [7, 8, 9, 7],
    [8, 9, 9, 4],
    [7, 4, 5, 7],
     ]
]
for bi in range(2):
    print("Group", bi+1)
    print("-"*32)
    print("Lesson:", end=" ")
   
    for li in range(4):
        print(f'  | ',li+1 , end="")
    print()
    for si in range(3):
        print(f'{students[si] }',end= "")
        for li in range(4):
           
            print(f' | ',marks [bi] [si] [li],end=" ")
        print()

    print()