ll = int(input("Enter the lower limit:"))
ul = int(input("Enter the upper limit:"))
for n in range(ll,ul):
    if n >1:
        for i in range(2,n):
            if n%i == 0:
                break
            else:
                print(n)
                break

