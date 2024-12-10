import csv
import os
import locale



def load_data(filename):
    products = [] #lista

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

def remove_products(products, id): 
    temp_product = None

    for product in products:
       if product['id'] == id:
           temp_product = product
           break
       
    if temp_product: 
       products.remove(temp_product)
       return f"{temp_product['name']} togs bort"
    else:
       return f"kunde inte hitta produkt"
       
def view_products(products): 
    product_list = []

    for index, product in enumerate(products, 1):
        product_info = f"{index}. (#{products['id']}) {products['name']} \t {product['desc']} \t {locale. currency(product['price'], grouping=True)}"


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
    product_list = []
    for product in products:
        product_info = f"Product: {product['name']} \t {product['desc']} \t {locale.currency(product['price'], grouping=True)}"
        product_list.append(product_info)

    return "\n".join(product_list)


#TODO: gör om så du slipper använda global-keyword
#TODO: write a function to return a specific product


locale.setlocale(locale.LC_ALL, 'sv_SE.UTF-8')  
products = load_data("db_products.osv")

while True: 
    os.system('cls')
    print(view_products(products)) 


    id = int(input("vilken produkt vill du bort? "))
        
        
    if id >= 1 and id <= len(products): 
        select = products[id-1]
        id = select['id']