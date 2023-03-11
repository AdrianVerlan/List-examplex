grades = {
    "English": 8,
    "Math": 9,
    "Informatic": 10
}
# k= keys, v = value, din cite am citit pe net in ciclu for pot fi folosite 2 variabile pentru
# a itera obiectele care contin perechi

for k, v in grades.items():
    print("|",end=" ")
    print(k,v)

    
    