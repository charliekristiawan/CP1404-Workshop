numOfItems = int(input("How much do you want to buy: "))

while numOfItems < 0:
    print("Invalid number")
    numOfItems = int(input("How much do you want to buy: "))

ShippingCost = int(input("Enter the shipping cost: "))
total = numOfItems*ShippingCost

if total > 100:
    totalCost = total - (total*0.1)
else:
    totalCost = total
print("The total cost is $" ,totalCost)