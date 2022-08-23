import random
minv= 1
maxv=6
roll = "yes"

while roll == "yes" or roll== "y":
    print("Rolling Dise....")
    print("Your value are :")
    print(random.randint(minv, maxv))
    roll = input("Roll again?")
