symbol=input("what symbol do you love  ")
number=int(input("Enter the size of the pattern: "))
i = 0
while i < number:
    j = 0
    while j < number:
        print("*", end=" ")
        j += 1
    print()
    i += 1

    