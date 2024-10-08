# define the menu of restaurants
menu = {
    'Pizza': 40.00,
    'Burger':50.00,
    'Chill Potato': 60.00,
    'Momos': 60.00,
    'Pasta': 45.00,
    'Cold Drink':20.00,
    'Chowmein' : 40.00,
    'Coffee' : 35.00,
    'Chhole Bature': 40.00,
}

#Greet
(" WELCOME TO FAST FOOD CAFE ")
(" Pizza : Rs 50.00\n Burger : Rs 30.00\n Chill Potato : Rs 70.00\n Momos: Rs 40.00\n Pasta : Rs 45.00\n Cold Drink : Rs 20.00\n Chowmein : Rs 60.00\n Coffee : Rs 35.00\n Cholle Bature : Rs 40.00")

order_total = 0

item1 = input("Enter the name of item you want to order = ")
if item1 in menu :
    order_total += menu[item1]
    (f"your item {item1} has been added to your order")

else:
    (f"Ordered item {item1} is not avaialable yet!!")

another_order = input("Do you want to add another item? (yes/no) ")
if another_order == "yes":
    item2 = input("enter the name of second item = ")
    if item2 in menu :
        order_total += menu[item2]
        (f"Item {item2} has been added to order")
    
    else:
        (f"Ordered item {item2} is not avaialable !!")

(f"The totalamount of itmes to pay is {order_total}")