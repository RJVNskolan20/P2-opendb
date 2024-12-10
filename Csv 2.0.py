import csv
import os
import locale
from time import sleep

# Load data from CSV file into the products list
def load_data(filename):
    products = []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            products.append({
                "id": int(row['id']),
                "name": row['name'],
                "desc": row['desc'],
                "price": float(row['price']),
                "quantity": int(row['quantity'])
            })
    return products

# Save products data back to CSV
def save_data(products, filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["id", "name", "desc", "price", "quantity"])
        writer.writeheader()
        writer.writerows(products)
    print(f"{bcolors.GREEN}Data successfully saved to {filename}{bcolors.DEFAULT}")


# Add a new product to the list
def add_product(products, name, desc, price, quantity):
    max_id = max(products, key=lambda x: x["id"])["id"] if products else 0
    new_id = max_id + 1
    products.append({"id": new_id, "name": name, "desc": desc, "price": price, "quantity": quantity})
    return f"{bcolors.GREEN}Lade till produkt: {new_id}{bcolors.DEFAULT}"


# View a specific product by ID
def view_product(products, id):
    for product in products:
        if product["id"] == id:
            return f"{bcolors.CYAN}Visar produkt: {product['name']} {product['desc']}{bcolors.DEFAULT}"
    return f"{bcolors.RED}Produkten hittas inte{bcolors.DEFAULT}"


# Remove a product by ID
def remove_product(products, id):
    # Find the product with the given ID
    temp_product = next((product for product in products if product["id"] == id), None)

    # If the product exists, remove it and return its details
    if temp_product:
        products.remove(temp_product)
        return (f"{bcolors.RED}Removed Product:\n"
                f"ID: {temp_product['id']}\n"
                f"Name: {temp_product['name']}\n"
                f"Description: {temp_product['desc']}\n"
                f"Price: {locale.currency(temp_product['price'], grouping=True)}\n"
                f"Quantity: {temp_product['quantity']}{bcolors.DEFAULT}")
    else:
        # If not found, show an error message
        return f"{bcolors.RED}Product with ID {id} not found.{bcolors.DEFAULT}"


# View all products in a formatted table
def view_products(products):
    if not products:
        return f"{bcolors.YELLOW}No products available.{bcolors.DEFAULT}"
   
    header = f"{bcolors.BOLD}{'#':<6} {'NAMN':<26} {'BESKRIVNING':<51} {'PRIS':<15} {'KVANTITET':<10}{bcolors.DEFAULT}"
    separator = "-" * 110
    rows = [
        f"{idx + 1:<5} {product['name']:<25} {product['desc']:<50} {locale.currency(product['price'], grouping=True):<14} {product['quantity']:<10}"
        for idx, product in enumerate(products)
    ]
    return "\n".join([header, separator] + rows)


def view_inventory(products):
    # Create the header for the table
    header = f"{bcolors.BOLD}{'ID':<6} {'NAME':<26} {'DESCRIPTION':<51} {'PRICE':<15} {'QUANTITY':<10}{bcolors.DEFAULT}"
    separator = "-" * 110  # line
   
    # Rows for each product
    rows = []

    for index, product in enumerate(products, 1):
        name = product['name']
        desc = product['desc']
        price = product['price']
        quantity = product['quantity']
       
        price = locale.currency(price, grouping=True)
        row = f"{index:<5} {name:<25} {desc:<50} {price:<14} {quantity:<10}"

        rows.append(row)
   
    # Combine header and rows
    inventory_table = "\n".join([header, separator] + rows)
   
    return f"{inventory_table}"

class bcolors:
    # ANSI escape sequences for terminal text formatting.
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    DEFAULT = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Set locale for price formatting
locale.setlocale(locale.LC_ALL, 'sv_SE.UTF-8')
os.system('cls' if os.name == 'nt' else 'clear')
products = load_data('db_products.csv')
print(view_products(products))

try:
    locale.setlocale(locale.LC_ALL, 'sv_SE.UTF-8')
except locale.Error:
    print("Locale not available. Defaulting to system locale.")


# Sort products by a specific key
def sort_products(products, key, reverse=False):
    """
    Sorts the products list based on the given key and order.
    :param products: List of product dictionaries.
    :param key: Key to sort by ('name', 'price', 'quantity').
    :return: Sorted list of products.
    """
    valid_keys = {"name": "name", "price": "price", "quantity": "quantity"}
    if key in valid_keys:
        products.sort(key=lambda x: x[valid_keys[key]], reverse=reverse)
        order = "descending" if reverse else "ascending"
        print(f"{bcolors.GREEN}Sorted by {key} in {order} order.{bcolors.DEFAULT}")
    else:
        print(f"{bcolors.RED}Invalid sorting key: {key}{bcolors.DEFAULT}")

def get_valid_price(prompt):
    """Prompt the user for a valid non-negative price."""
    while True:
        try:
            price = float(input(prompt))
            if price < 0:
                raise ValueError("Price cannot be negative.")
            return price
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a valid non-negative price.")

def get_valid_quantity(prompt):
    """Prompt the user for a valid non-negative quantity."""
    while True:
        try:
            quantity = int(input(prompt))
            if quantity < 0:
                raise ValueError("Quantity cannot be negative.")
            return quantity
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a valid non-negative quantity.")

        save_data(products, 'db_products.csv')    

# Main loop
# Main loop
while True: 
    print("\nMain Menu:")
    print("1. Add Product")
    print("2. View Product by ID")
    print("3. Remove Product")
    print("4. Exit")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        name = input("Product Name: ")
        desc = input("Description: ")
        try:
            price = float(input("Price: "))
            quantity = int(input("Quantity: "))
            print(add_product(products, name, desc, price, quantity))
        except ValueError:
            print("Please enter valid numbers for price and quantity.")
        

    elif choice == "2":
        try:
            index = int(input("Enter product ID: "))
            print(view_product(products, index))
        except ValueError:
            print("Please enter a valid numeric product ID.")
            

    elif choice == "3":
        try:
            index = int(input("Enter product ID to remove: "))
            print(remove_product(products, index))
        except ValueError:
            print("Please enter a valid numeric product ID.")
            

    elif choice == "4":
        save_data(products, 'db_products.csv')
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid option. Please choose again.")

save_data(products, 'db_products.csv')    

# Main loop
while True:
    choice = input("Vill du (L)ägg till produkt, (V)isa eller (T)a bort en produkt? ").strip().upper()

    if choice == "L":
        name = input("Namn på produkt: ")
        desc = input("Beskrivning: ")
        price = float(input("Pris: "))
        quantity = int(input("Antal: "))
        print(add_product(products, name, desc, price, quantity))

    elif choice in ["V", "T"]:
        try:
            index = int(input("Enter product ID: "))
            if choice == "V":
                print(view_product(products, index))
            elif choice == "T":
                print(remove_product(products, index))
        except ValueError:
            print(f"{bcolors.RED}Välj en produkt-ID med siffror.{bcolors.DEFAULT}")
            sleep(0.5)

def load_data(filename):
    try:
        with open(filename, 'r') as file:
            return list(csv.DictReader(file))
    except FileNotFoundError:
        print(f"{bcolors.RED}File {filename} not found. Starting with an empty inventory.{bcolors.DEFAULT}")
        return []
    except Exception as e:
        print(f"{bcolors.RED}Error loading data: {e}{bcolors.DEFAULT}")
        return []

def exit_program(products):
    save_data(products, 'db_products.csv')
    print(f"{bcolors.GREEN}Data saved. Exiting program.{bcolors.DEFAULT}")
    exit(0)

    save_data(products, 'db_products.csv')
