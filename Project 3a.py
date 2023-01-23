sum = 0
for num in range(1, 4): # range(1, 4) is changeable. It depends on how many numbers the user need to enter.
    numbers = int(input("please enter the number"))
    sum += num
if sum % 2 == 0:
    print("even")
else:
    print("odd")

