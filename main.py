count = 5

for i in range(count):
    print(" " * (count-i-1), end=" ")
    for j in range(i+1):
        print("* ", end="")
    print()