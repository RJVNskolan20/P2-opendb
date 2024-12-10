import csv
import os
import locale



def load_data(filename):
<<<<<<< HEAD
    products = [] #lista

=======
    products = [] 
    
>>>>>>> 1bcfe247a0afa3a0142b6b26398324d2841dea6d
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            id = int(row['id'])
            name = row['name']
            desc = row['desc']
            price = float(row['price'])
            quantity = int(row['quantity'])

            products.append(
                {                   #dictionary
                    "id": id,       #"keys" / nycklar : värde
                    "name": name,
                    "desc": desc,
                    "price": price,
                    "quantity": quantity
                }
            )
    return products
<<<<<<< HEAD



def get_product(products, id):
    if id < 0 or id > len(products) - 1:
        return "produkten hittas inte"
    else: 
        return f"{products[id]['name']} {products[id]['desc']}"
    
def remove_product(products, id):
    print(id)
    temp_product = products[id]["name"]
    products.pop(id)
    return f"product: {id} was removed"

def get_products(products):
=======
    
def view_products(products):
>>>>>>> 1bcfe247a0afa3a0142b6b26398324d2841dea6d
    product_list = []
     #TODO: gör en nummerlista med enumerate (att använda id kommer inte fungera i längden)
     
    for product in products:
<<<<<<< HEAD
        product_info = f"Product: {product['name']} \t {product['desc']} \t {locale.currency(product['price'], grouping=True)}"
=======
        product_info = f"(#{product['id']}) {product['name']} \t {product['desc']} \t {locale.currency(product['price'], grouping=True)}"
>>>>>>> 1bcfe247a0afa3a0142b6b26398324d2841dea6d
        product_list.append(product_info)

    return "\n".join(product_list)


<<<<<<< HEAD
#TODO: gör om så du slipper använda global-keyword
#TODO: write a function to return a specific product
=======
#TODO: skriv en funktion som returnerar en specifik produkt med hjälp av id
#TODO: skriv en funktion som tar bort en specifik produkt med hjälp av id

>>>>>>> 1bcfe247a0afa3a0142b6b26398324d2841dea6d


locale.setlocale(locale.LC_ALL, 'sv_SE.UTF-8')  

<<<<<<< HEAD

os.system('cls')
products = load_data('db_products.csv')

print(get_products(products))

while True: 
    try: 
        print(get_products(products))
        id = int(input("vilken? "))
        print(remove_product(products, id ))

    except: 
        print("Sweet summer child du behöver skriva siffror")
        continue
=======
while True:
    os.system('cls')
    products = load_data('db_products.csv')
    print(view_products(products))

    id = int(input("Vilken produkt vill du visa? "))
>>>>>>> 1bcfe247a0afa3a0142b6b26398324d2841dea6d
