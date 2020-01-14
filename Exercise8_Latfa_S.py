username = input("Username : ")
password = input("Password : ")
if username == "lala" and password == "1212312121":
    print("Login Success!")
    print("____________lalaPhoneShop_____________\n")
    print("1. iPhone11 (64 GB)          : 24,900THB")
    print("2. iPhone11 (128 GB)         : 26,900THB")
    print("3. iPhone11 (256 GB)         : 30,900THB")
    print("4. iPhone11 Pro(64 GB)       : 35,900THB")
    print("5. iPhone11 Pro(256 GB)      : 41,900THB")
    print("6. iPhone11 Pro(512 GB)      : 48,900THB")
    print("7. iPhone11 Pro Max(64 GB)   : 39,900THB")
    print("8. iPhone11 Pro Max(256 GB)  : 45,900THB")
    print("9. iPhone11 Pro Max(512 GB)  : 52,900THB")
    print("----------------------------------------")
    userSelected = int(input("Select product : "))
    if userSelected == 1:
        quantity = int(input("Quantity : "))
        totalPrice = quantity*24900
        print("Total : ",totalPrice,"THB")
    elif userSelected == 2:
        quantity = int(input("Quantity : "))
        totalPrice = quantity*26900
        print("Total : ",totalPrice,"THB")
    elif userSelected == 3:
        quantity = int(input("Quantity : "))
        totalPrice = quantity*30900
        print("Total : ",totalPrice,"THB")
    elif userSelected == 4:
        quantity = int(input("Quantity : "))
        totalPrice = quantity*35900
        print("Total : ",totalPrice,"THB")
    elif userSelected == 5:
        quantity = int(input("Quantity : "))
        totalPrice = quantity*41900
        print("Total : ",totalPrice,"THB")
    elif userSelected == 6:
        quantity = int(input("Quantity : "))
        totalPrice = quantity*48900
        print("Total : ",totalPrice,"THB")
    elif userSelected == 7:
        quantity = int(input("Quantity : "))
        totalPrice = quantity*39900
        print("Total : ",totalPrice,"THB")
    elif userSelected == 8:
        quantity = int(input("Quantity : "))
        totalPrice = quantity*45900
        print("Total : ",totalPrice,"THB")
    elif userSelected == 9:
        quantity = int(input("Quantity : "))
        totalPrice = quantity*52900
        print("Total : ",totalPrice,"THB")
    print("------Thank you!------")
else:
    print("wrong username or password!")
