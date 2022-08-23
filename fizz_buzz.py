start = int(input("Enter start: " ))
end = int(input("Enter end: " ))

for i in range(start,end):
    if (i % 3 ==0) and (i % 5 == 0):
        print("FizzBuzz")
    elif i % 3 ==0:
        print("Fizz")
    elif i % 3 ==0:
        print("Buzz")
    else:
        print(i)
