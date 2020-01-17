num = int(input("Number: "))
for row in range(num):
    for col in range(num-row-1):
        print(end=" ")
    for col in range(row+1):
        print("*",end=" ")
    print("\r")