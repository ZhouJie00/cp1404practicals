#work out the total price for a number of items,
# each with different prices.


item_number = int(input("Number of items: "))

while item_number <0:
    item_number = int(input("Number of items: "))

total_price = 0
for i in range(item_number): #0,1,2
    price = float(input("Price of item: "))
    total_price += price


if  total_price > 100:
    total_price = total_price - (total_price*0.10)
print(f"Total price for {item_number} items is ${total_price:.2f}")


# + Error checking (input validation loop)
