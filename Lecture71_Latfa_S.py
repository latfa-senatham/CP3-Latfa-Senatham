menuList = []
priceList = []

def showBill():
    print("-----LaLa Restaurant-----")
    totalPrice = 0
    for number in range(len(menuList)):
        print(menuList[number],priceList[number],"THB")
        totalPrice += priceList[number]
    print("-------------------------")
    print("Total Price: ",totalPrice,"THB")

while True:
    menuName = input("Please Enter Menu: ")
    if(menuName.lower()=="exit"):
        break
    else:
        menuPrice = int(input("Price: "))
        menuList.append(menuName)
        priceList.append(menuPrice)
print(menuList,priceList)
showBill()