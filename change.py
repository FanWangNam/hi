cents = int(input("Please enter an amount in cents less than a dollar."))
print(cents)
print("Your change will be: ")
Q = cents // 25
D = (cents - (Q * 25)) // 10
N = (cents - (Q * 25) - (D * 10)) // 5
P = (cents - (Q * 25) - (D * 10) - (N * 5)) // 1
print("Q:", Q)
print("D:", D)
print("N:", N)
print("P:", P)
