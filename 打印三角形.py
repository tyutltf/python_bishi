for i in range(10):
    for j in range(0, 10 - i):
        print(end=" ")
    for k in range(10 - i, 10):
        print("*", end=" ")

    print("")

for l in range(10):
    for m in range(l):
        print(" ",end="")
    for n in range(10-l):
        print("*",end=" ")
    print("")
