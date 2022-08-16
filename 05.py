n = [500, 100, 50, 20, 10, 5, 2, 1]

a = int(input("Enter the amount: "))
print("Total Number of Notes:")
for i in range(8):

    print(n[i], ":", int(a / n[i]))

    a = a % n[i]
