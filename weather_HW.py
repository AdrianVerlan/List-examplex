from os import system
system("cls")
days = ["MO","TU","Wd","TH","FR","SA","SU"]
temps =[10.9, 11.7, 17.9, 8, -18, 15.0, -6]
i =0
while i<7:
    if temps[i]<=0:
        sign="*"
    else: sign =" "
    print(f"|",sign, days[i],"|",temps[i])
    i+=1