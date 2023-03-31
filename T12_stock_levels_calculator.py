# T12 COMPULSORY TASK CAFE MENU ITEMS

# (1) Creating a list called menu, which should contain at least 4 items in the cafe.

menu = ["Tea", "Coffee", "Scones", "Cake"]

# (2) Creating a dictionary called stock, which should contain the stock value for each item on your menu.

stock = {"Tea" : 600, "Coffee" : 1000, "Scones" : 50, "Cake" : 30}

# (3) Creating a dictionary called price, which should contain the prices for each item on your menu.

price = {"Tea" : 1.50 , "Coffee" : 4.00, "Scones" : 3.50, "Cake" : 4.50}

# (4) Calculating the total_stock worth in the cafe.

total_stock = 0

for each in menu:
    total_stock += stock[each] * price[each]

# (5) Printing out the result of the calculation.

print ("-" * 50)
print(f"The total stock value is: £ {total_stock:.2f}")
print ("-" * 50)
