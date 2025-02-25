print("Welcome to Byte and Brew Cafe, how can I help you today?")
print("Please have a look at our food and drinks menu!!")
 
order_complete = False
total_price = 0.0  # This will track the total price of the order
items_ordered = []  # This will track the items ordered
 
# Initialize the data
menu_items = {          #appropriate variable
    'food': ['sandwich', 'cake', 'croissants', 'muffin', 'danish', 'bagel', 'chocolate cookie', 'brownie'],  # use of lists
    'drinks': ['latte', 'tea', 'orange juice', 'apple juice', 'black coffee', 'flat white', 'chai tea', 'cappuccino']
}
book_list = ['The alchemist', 'a song of ice and fire', 'moby dick', 'pride and prejudice', 'the hobbit', 'salems lot', 'the war horse']
 
# def display_menu_and_books():                 # Function to display the menu
#     print("Food Menu:", menu_items['food'])
#     print("Drinks Menu:", menu_items['drinks'])
#     print("Books Available:", book_list)
def display_menu_and_books():
    print("\n*** Welcome to Byte and Brew Cafe! ***")
    print("Here's our menu:")
    print("\n--- Food Menu ---")
    for food in menu_items['food']:
        print(f"{food.title()}")
    print("\n--- Drinks Menu ---")
    for drink in menu_items['drinks']:
        print(f"{drink.title()}")
    print("\n--- Books Available ---")
    for book in book_list:
        print(f"{book.title()}")
    print("\n")
 
 
# Handle food ordering
def handle_food_order():
    global total_price
    while True:
        food = input("What food would you like to order from the cafe? \n").lower()
 
        # Check for available items and update total price accordingly
        if food == 'sandwich':                       #if starts the items whilst elif goes through all the items in the list and else ends it
            print("You have bought a sandwich!")
            total_price += 4.50
            items_ordered.append("sandwich")
        elif food == 'cake':
            print("You have bought a cake!")
            total_price += 3.00
            items_ordered.append("cake")
        elif food == 'croissant':
            print("You have bought a croissant!")
            total_price += 1.50
            items_ordered.append("croissant")
        elif food == 'muffin':
            print("You have bought a muffin!")
            total_price += 2.00
            items_ordered.append("muffin")
        elif food == 'danish':
            print("You have bought a danish!")
            total_price += 2.00
            items_ordered.append("danish")
        elif food == 'bagel':
            print("You have bought a bagel!")
            total_price += 2.00
            items_ordered.append("bagel")
        elif food == 'chocolate cookie':
            print("You have bought a chocolate cookie!")
            total_price += 2.50
            items_ordered.append("chocolate cookie")
        elif food == 'brownie':
            print("You have bought a brownie!")
            total_price += 1.50
            items_ordered.append("brownie")
        else:
            print("Sorry, we don't have that item. Please select from the menu.")
            continue
 
        # Ask if they want to order more food or move to drinks
        more_food = input("Would you like to order more food? (yes/no): ").lower()
        if more_food != 'yes':
            break
 
# Handle drink ordering
class Drink:                         #use of class
    def __init__(self, small_size, medium_size, large_size):
        # Assign the drink cup size
        self.small_size = small_size
        self.medium_size = medium_size
        self.large_size = large_size
 
    def order_small(self):
        print(f"{self.small_size} here is a small cup")
 
    def order_medium(self):
        print(f"{self.medium_size} here is a medium cup")
 
    def order_large(self):
        print(f"{self.large_size} here is a large cup")
 
# Drink order handler
def handle_drink_order():
    global total_price
    while True:           #while loop
        drink = input("What drink would you like to order from the cafe?").lower()
       
        if drink == 'latte':                         #if statement used
            print("You have bought a latte")
            size = input("What size drink would you like? (small - £3.00  medium - £3.50  large - £4.00): ").lower()
            if size == 'small':
                total_price += 3.00
                items_ordered.append("latte (small)")
            elif size == 'medium':
                total_price += 3.50
                items_ordered.append("latte (medium)")
            elif size == 'large':
                total_price += 4.00
                items_ordered.append("latte (large)")
        elif drink == 'tea':
            print("You have bought a tea!")
            size = input("What size drink would you like? (small - £2.00  medium - £2.50  large - £3.00): ").lower()
            if size == 'small':
                total_price += 2.00
                items_ordered.append("tea (small)")
            elif size == 'medium':
                total_price += 2.50
                items_ordered.append("tea (medium)")
            elif size == 'large':
                total_price += 3.00
                items_ordered.append("tea (large)")
        elif drink == 'apple juice':
            print("You have bought apple juice")
            total_price += 1.50
            items_ordered.append("apple juice")
        elif drink == 'orange juice':
            print("You have bought orange juice")
            total_price += 1.50
            items_ordered.append("orange juice")
        elif drink == 'black coffee':
            print("You have bought a black coffee")
            size = input("What size drink would you like? (small - £1.00  medium - £1.50  large - £2.00): ").lower()
            if size == 'small':
                total_price += 1.00
                items_ordered.append("black coffee(small)")
            elif size == 'medium':
                total_price += 1.50
                items_ordered.append("black coffee (medium)")
            elif size == 'large':
                total_price += 2.00
                items_ordered.append("black coffee (large)")
        elif drink == 'flat white':
            print("You have bought a flat white")
            size = input("What size drink would you like? (small - £1.00  medium - £1.50  large - £2.00): ").lower()
            if size == 'small':
                total_price += 1.00
                items_ordered.append("flat white(small)")
            elif size == 'medium':
                total_price += 1.50
                items_ordered.append("flat white (medium)")
            elif size == 'large':
                total_price += 2.00
                items_ordered.append("flat white (large)")
        elif drink == 'chai tea':
            print("You have bought a chai tea")
            size = input("What size drink would you like? (small - £2.50  medium - £3.00  large - £3.50): ").lower()
            if size == 'small':
                total_price += 2.50
                items_ordered.append("chai tea(small)")
            elif size == 'medium':
                total_price += 3.00
                items_ordered.append("chai tea (medium)")
            elif size == 'large':
                total_price += 3.50
                items_ordered.append("chai tea (large)")
        elif drink == 'cappuccino':
            print("You have bought a cappuccino")
            size = input("What size drink would you like? (small - £3.50  medium - £4.00  large - £4.50): ").lower()
            if size == 'small':
                total_price += 3.50
                items_ordered.append("cappuccino (small)")
            elif size == 'medium':
                total_price += 4.00
                items_ordered.append("cappuccino (medium)")
            elif size == 'large':
                total_price += 4.50
                items_ordered.append("cappuccino (large)")                
               
 
        else:
            print("Sorry, we don't have that drink. Please select from the menu.")
            continue
       
        more_drink = input("Would you like to order more drinks? (yes/no): ").lower()   #boolean
        if more_drink != 'yes':
            break
 
# Handle book ordering
def handle_book_order():
    global total_price, items_ordered
    book_list = ['The alchemist', 'a song of ice and fire', 'moby dick', 'pride and prejudice', 'the hobbit', 'salems lot', 'the war horse']
    while True:
        book = input("Would you like to order a book from the cafe? yes/no\n").lower()
        if book == "yes":  
         print("Books Available:", book_list)
         wanted_book=input("Enter the book(s) you would line to order. ").strip().lower()
         if wanted_book in [b.lower() for b in book_list]:
             print(f"You have ordered the book '{wanted_book.title()}'!")
             total_price += 10.00  # Example price for a book     #london book prices are scary
             items_ordered.append(wanted_book.title())
         else:
            print("Sorry, that book is not available. Please choose from the list.")
  # If the customer doesn't want to order a book
        elif book == "no":
            print("Moving on")
            break  # Exit the loop if they don't want to order a book
        else:
             print("Invalid input, please answer with 'yes' or 'no'.")
 
# Collect customer information
def collect_customer_info():         #dictionary used
    print("\nPlease provide your details to complete the order.")
    firstname = input("Enter your first name: ").capitalize()
    table_number = input("Enter your table number: ")
   
    return {
        "firstname": firstname,
        "table number": table_number
    }
 
# Main order process
display_menu_and_books()
handle_food_order()
handle_drink_order()
handle_book_order()
 
# Collect customer information
customer_info = collect_customer_info()
 
# Final Order Summary
print("\nOrder Summary:")
print("Customer:", customer_info['firstname'])
print("Table Number:", customer_info['table number'])
print("Items Ordered:", ", ".join(items_ordered))
print(f"Total Price: £{total_price:.2f}")
 
# Ask for confirmation before finalizing the order
order_complete = input("Would you like to complete your order? (yes/no): ").lower()
if order_complete == 'yes':
    print("Thank you for your order!")
    print(f"Your order will be served to table {customer_info['table number']}. Enjoy your order!")
else:
    print("Order is abandoned. Have a great day!")
 