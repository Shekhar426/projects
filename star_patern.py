count = 4

for i in range(count):
    # print(" " * (count-i), end = "")
    for j in range(i+1):
        print("*", end = "")
    print()
second_count = count-1

for k in range(second_count):
    print(" " * (k+1), end="")
    for l in range(second_count-k):
        print("*", end = '')
    print()
