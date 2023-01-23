number = int(input("How many integers would you like to enter?"))
print(number)
print("Please enter", number, "integers.")

max = 0
min = 0
for item in range(1, number + 1):
    integer = int(input())
    print(integer)

    if item == 0:
        min = integer
    elif integer > max:
        max = integer
    else:
        min = integer
print("min:", min)
print("max:", max)






