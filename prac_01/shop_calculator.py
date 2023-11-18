#work out the total price for a number of items,
# each with different prices.


itemNumber =  int(input("Number of items: "))

while itemNumber <0:
    itemNumber = int(input("Number of items: "))

totalPrice = 0
for i in range(itemNumber): #0,1,2
    price = float(input("Price of item: "))
    totalPrice+= price


if  totalPrice > 100:
    totalPrice = totalPrice - (totalPrice*0.10)
print(f"Total price for {itemNumber} items is ${totalPrice:.2f}")


# + Error checking (input validation loop)
