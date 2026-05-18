from math import sqrt

ll = int(input("Enter the lower limit:"))
ul = int(input("Enter the upper limit:"))
for n in range(ll, ul):
    if n > 1:
        isPrime = True
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                isPrime = False
                break

        if isPrime:
            print(n)
    else:
        print("not a valid input")
