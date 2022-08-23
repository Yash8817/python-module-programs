import random
while True:
    print("Enter Choise: 1...Roll  or  2...Exit")
    ch = int(input("Enter choise..."))
    if(ch==1):
        ran = random.randint(1,6)
        print("Value :",ran)
    else:
        break

