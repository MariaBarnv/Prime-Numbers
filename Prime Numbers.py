N=1000
x = 1
print("The prime numbers: ")
for x1 in range(x, N + 1):
    if x1 > 1:
        for y in range(2, x1):
            if (x1 % y) == 0:
                break
        else:
            print(x1)

