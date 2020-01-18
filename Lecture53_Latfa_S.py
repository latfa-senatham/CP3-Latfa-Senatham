def vatCalculate():
    totalPrice = float(input("Total price: "))
    vat = float(input("VAT(%): "))
    result = totalPrice + (totalPrice*vat/100)
    return "Price including vat: "+str(result)
print(vatCalculate())