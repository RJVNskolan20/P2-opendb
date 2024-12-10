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
    print(f"Data successfully saved to {filename}")

# Add a new product to the list
def add_product(products, name, desc, price, quantity):
    max_id = max(products, key=lambda x: x["id"])["id"] if products else 0
    new_id = max_id + 1
    products.append({"id": new_id, "name": name, "desc": desc, "price": price, "quantity": quantity})
    return f"Lade till produkt: {new_id}"

# View a specific product by ID
def view_product(products, id):
    for product in products:
        if product["id"] == id:
            return f"Visar produkt: {product['name']} {product['desc']}"
    return "Produkten hittas inte"

# Remove a product by ID
def remove_product(products, id):
    # Find the product with the given ID
    temp_product = next((product for product in products if product["id"] == id), None)

    # If the product exists, remove it and return its details
    if temp_product:
        products.remove(temp_product)
        return (f"Removed Product:\n"
                f"ID: {temp_product['id']}\n"
                f"Name: {temp_product['name']}\n"
                f"Description: {temp_product['desc']}\n"
                f"Price: {locale.currency(temp_product['price'], grouping=True)}\n"
                f"Quantity: {temp_product['quantity']}")
    else:
        # If not found, show an error message
        return f"Product with ID {id} not found."

# View all products in a formatted table
def view_products(products):
    if not products:
        return "No products available."
    
    header = f"{'#':<6} {'NAMN':<26} {'BESKRIVNING':<51} {'PRIS':<15} {'KVANTITET':<10}"
    separator = "-" * 110
    rows = [
        f"{idx + 1:<5} {product['name']:<25} {product['desc']:<50} {locale.currency(product['price'], grouping=True):<14} {product['quantity']:<10}"
        for idx, product in enumerate(products)
    ]
    return "\n".join([header, separator] + rows)

def view_inventory(products):
    # skapa sidhuvudet av tabellen:
    header = f"{'ID':<6} {'NAME':<26} {'DESCRIPTION':<51} {'PRICE':<15} {'QUANTITY':<10}"
    separator = "-" * 110           #linje
    
    # rader för varje produkt:
    rows = []

    for index, product in enumerate(products, 1):
        name = product['name']
        desc = product['desc']
        price = product['price']
        quantity = product['quantity']
        
        price = locale.currency(price, grouping=True)
        row = f"{index:<5} {name:<25} {desc:<50} {price:<14} {quantity:<10}"

        rows.append(row)
    
    # kombinera sidhuvud och rader:
    inventory_table = "\n".join([header, separator] + rows)
    
    return f"{inventory_table}"

class bcolors:
    #ANSI escape sequences for terminal text formatting.

    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    DEFAULT = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    # @staticmethod
    # def color_text(text, color):
    #     return f"{color}{text}{BColors.DEFAULT}"

# Set locale for price formatting
locale.setlocale(locale.LC_ALL, 'sv_SE.UTF-8')
os.system('cls' if os.name == 'nt' else 'clear')
products = load_data('db_products.csv')
print(view_products(products))

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
            print("Välj en produkt-ID med siffror.")
            sleep(0.5)
    
    save_data(products, 'db_products.csv')

    