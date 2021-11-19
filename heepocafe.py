
from datetime import datetime
import re  

print(datetime.now())


#Menu dicts 
menu_category = {1: "Set Meals", 2: "Main Course ", 3: "Sides", 4: "Drinks ", 5: "Desserts"}
set_meals_menu = {1: ["Chicken Burger Set", 14.65], 2: ["Fish Burger Set", 13.65], 3: ["Beef Burger Set", 16.65], 4: ["Chicken Nuggets Set", 10.65], 5: ["Fried Chicken Set", 13.65]} 
main_course_menu = {1: ["Chicken Burger", 10.95], 2: ["Fish Burger", 9.95], 3: ["Beef Burger", 12.95], 4: ["Chicken Nuggets", 6.95], 5: ["Fried Chicken", 9.95]} 
sides_menu = {1: ["Friend Fries", 2.95], 2: ["Caesar Salad", 2.65], 3: ["Mushroom Soup", 3.05], 4: ["Nachos", 2.95], 5: ["Potato Wedges", 3.25], 6: ["Buttered Corn", 2.65]} 
drinks_menu = {1: ["Pop Drinks (Coca-Cola/ Sprite/ Mountain Dew/ Pepsi)", 3.25], 2: ["Hot Choclate", 3.75], 3: ["Iced-Chocolate", 3.95], 4: ["Banana Milkshake", 5.25], 5: ["Strawberry Milkshake", 5.25]}  

# Customer enter main page 
customer_input = input('Hi! Please tell us your name!\n')

def delivery_method():
    while True:
        choice = input(f'''Hi {customer_input} ! Would you like to:\n 1)Take away \n 2)Dine-in \n 3)Delivery \n''')
        if choice == '1' or choice == '2': 
            print("Great! Please continue with your order!")
            break 
        elif choice == '3':
            customer_address = input(f"Great! Please tell us your desired delivery address! \n") 
            print(f'''You delivery address will be {customer_address}. \n''')
            break   
        else:
            print("Please choose between 1, 2, and 3 only.")
            continue

# Menu tour
cart_for_set_meals = []  
def menu_tour():
    while True:
        print("Menu Category:") 
        print(menu_category)
        menu = input(f''' Please tell us which menu are you interested to explore? \n''')
        if menu == '1':
            print("Here's our set meals menu! Please select your favourite set meal!")
            print(set_meals_menu)
            while True:
                set_meal_select = int(input(f'''Enter your selection or input '0' to return to Menu Category:'''))
                if set_meal_select == 0:
                    continue
                if 6 > int(set_meal_select) > 0:
                    cart_for_set_meals.append(set_meal_select)
                if set_meal_select not in range(6): 
                    print("Please select number from 1 to 5 ONLY!")
                    continue
                break
# Need to except ValueError as print select number from 1-5 only (18/11) 

        elif menu == '2':
            print("Here's our main course menu!")
            print(main_course_menu)
            break
        elif menu == '3':
            print("Here's our sides menu!")
            print(sides_menu)
            break 
        elif menu == '4': 
            print("Here's our drinks menu!") 
            print(drinks_menu)
            break
        else:
            print("Please select '1', '2', '3' or '4' ONLY!")
            continue 
 

# Main 
delivery_method()
menu_tour() 








############# SPLIT LINE ###################
 
# if second_step == '1': 
#     print ("Great! Please see our special set menu here: \n" + menuA + "\n" + menuB + "\n" + menuC )
# elif second_step == '2': 
#     print ("Great! Please see our special set menu here: \n" + menuA + "\n" + menuB + "\n" + menuC )
# elif second_step == '3':
#     customer_address = input (f"Great! Please tell us your full address \n") 
#     print(f"Your address is " + customer_address + ".\n Please see our special set menu here: \n" + menuA + "\n" + menuB + "\n" + menuC )
# else:
#     print("Please enter 1,2, or 3 only") 


# customer_choice = input(f'Please choose your set meal \n (A/B/C) \n')
# if customer_choice == 'a':
#     print("Set A")
# elif customer_choice == 'b':
#     print("Set B")
# elif customer_choice == 'c':
#     print("Set C")
# else: 
#     print("Please selected A / B / C only")

# final_choice = customer_choice


# drink_choice = input(f'Please choose your drink: \n 1)Coca-Cola \n 2)100-Plus \n 3)Sprite \n 4)Apple Juice \n 5)Orange Juice \n')
# if drink_choice == '1':
#     print("Coca-Cola")
# elif drink_choice == '2':
#     print("100-Plus")
# elif drink_choice == '3':
#     print("Sprite")
# elif drink_choice == '4':
#     print("Apple Juice")
# elif drink_choice == '5':
#     print("Orange Juice")
# else:
#     print("Please select 1, 2, 3, 4, or 5 only")
# side_choice = input(f'Please choose you side: \n 1)Fries \n 2)Caesar Salad \n')
# if side_choice == '1':
#     print("Fries")
# elif side_choice == '2':
#     print("Caesar Salad")
# else:
#     print("Please select 1 or 2 only")

# order_quantity = input(f'Please indicate quantity \n')
# print("You ordered " + order_quantity + " " + customer_choice) 

# if final_choice == a:
#     price = 15.90 

# if final_choice == b: 
#     price = 18.90

# if final_choice == c: 
#     price = 17.90

# print("Total = " + price* order_quantity + " dollars.") 
