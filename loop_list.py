# Initialize the counter
counter = 1

# While loop to print the first 25 integers
while counter <= 25:
    print(counter)
    counter += 1
    
    
    
    
gen = factorial_gen(5)

for result in gen:
    pass

print(f"Factorial of {5} is: {result}")


Initialize an array of numbers
numbers = [12, -7, 5, -3, 9, -10, 6, 0]


numbers = [num for num in numbers if num >= 0]

print("Array without negative numbers:", numbers)



def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 3

celsius_temps = input("Enter temperatures in Celsius, separated by commas: ")


celsius_list = [float(temp) for temp in celsius_temps.split(",")]

index = 0
fahrenheit_list = []

# Use a while loop to convert each Celsius temperature to Fahrenheit
while index < len(celsius_list):
    fahrenheit = celsius_to_fahrenheit(celsius_list[index])
    fahrenheit_list.append(fahrenheit)
    index += 1

# Print the converted temperatures in Fahrenheit
print("Converted temperatures in Fahrenheit:", fahrenheit_list)

         
         
 # Initialize an array of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


numbers = [num for num in numbers if num % 2 == 0]


print("Array without odd numbers:", numbers)        








# Function to insert a value at a specific index in an array
def insert_value(arr, index, value):
    # Insert the value at the specified index
    arr.insert(index, value)
    return arr

# Example usage
my_array = [10, 20, 30, 40]
index = 2
value = 25

# Insert value and print the modified array
modified_array = insert_value(my_array, index, value)
print("Modified Array:", modified_array)




# # Shopping cart program using array methods

# # Initialize an empty shopping cart (list of items)
shopping_cart = []

# Function to add an item to the cart
def add_item(name, quantity, price):
    # Check if the item already exists in the cart
    for item in shopping_cart:
        if item[0] == name:
            # If the item exists, update the quantity
            item[1] += quantity
            print(f"Updated {name}'s quantity to {item[1]}.")
            break
    else:
        # If the item doesn't exist, append it to the list
        shopping_cart.append([name, quantity, price])
        print(f"Added {quantity} of {name} to the cart.")
    
    print_cart()

# Function to remove an item from the cart
def remove_item(name):
    # Iterate over the cart and remove the item by name
    for item in shopping_cart:
        if item[0] == name:
            shopping_cart.remove(item)
            print(f"Removed {name} from the cart.")
            break
    else:
        print(f"{name} not found in the cart.")
    
    print_cart()

# Function to update the quantity of an item
def update_quantity(name, new_quantity):
    # Iterate over the cart and update the quantity of the item
    for item in shopping_cart:
        if item[0] == name:
            item[1] = new_quantity
            print(f"Updated {name}'s quantity to {new_quantity}.")
            break
    else:
        print(f"{name} not found in the cart.")
    
    print_cart()

# Function to print the cart's contents
def print_cart():
    if not shopping_cart:
        print("The cart is empty.")
    else:
        print("\nShopping Cart Contents:")
        for item in shopping_cart:
            print(f"{item[0]} - Quantity: {item[1]}, Price per item: ${item[2]:.2f}")
    print("-" * 30)

# Example usage
add_item("Apple", 3, 0.50)    # Adds 3 apples
add_item("Banana", 2, 0.30)   # Adds 2 bananas
update_quantity("Apple", 5)   # Updates the quantity of apples to 5
remove_item("Banana")         # Removes bananas from the cart
add_item("Orange", 4, 0.60)   # Adds 4 oranges



