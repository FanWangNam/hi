num = int(input("please enter a positive integer: "))
for item in range(1, num+1):
    if num % item == 0:
        print(item)
