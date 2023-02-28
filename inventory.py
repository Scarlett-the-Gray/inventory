from tabulate import tabulate

class Shoes:
#create a class named Shoes with the following attributes:
#country, code, product, cost, quantity

    def __init__(self, country, code, product, cost, quantity):# self -  access attributes and methods of the class in python
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

#________________________________________________________________________________________
# define functions inside the class
#get_cost, get_quantity, get_country,  get_code ,get_product, set_quantity, __str__

    def get_cost(self):
        return self.cost
    def get_quantity(self):
        return self.quantity
    def get_country(self):
        return self.country
    def get_code(self):
        return self.code  
    def get_product(self):
        return self.product
    def set_quantity(self, new_quant):
        self.quantity = new_quant

    def __str__(self):
        return f"{self.country},{self.code},{self.product},{self.cost},{self.quantity}\n".upper()

#_________________________________________________________________________________________
inventory_read = open("inventory.txt", "r")#open txt doc
inventory_write = open("inventory.txt", "a+")#write to txt doc - new input

items_list = []# create a variables with an empty list
shoe_obj = []

#_________________________________________________________________________________________
#define functions outside the class
#read_shoes_data
#capture_shoes
#view_all
#re_stock
#search_shoe
#value of shoes
#overstocked-shoes for sale

#_____________________________#read_shoes_data
def read_shoes_data():
    file = None
    try:
        for lines in inventory_read:
            strip_lines = lines.strip("\n")
            split_lines = strip_lines.split(",")
            items_list.append(split_lines)

        for i in range(1, len(items_list)):
            array = items_list[i]
            shoe1 =  Shoes(array[0], array[1], array[2], array[3], int(array[4]))
            shoe_obj.append(shoe1)
            
    except FileNotFoundError as error:
        print("\n       Error messagae:  File not found\n")
        print(error)

    finally:
        if file is not None:
            file.close()

#_______________________________#capture_shoes
#input of new stock
#info needed: country,code,product,name,cost and quantity
#acknowledge captured stock
def capture_shoes():  
    file = None
    try:
        new_country = input("Enter country name: \n")
        new_code = input("Enter code of product: \n")
        new_product = input("Enter name of product:\n")
        new_cost = int(input("Enter cost of product.  Do not include currency code.: \n"))
        new_quantity = int(input("Enter quantity of product received.:\n"))

        new_shoe = Shoes(new_country, new_code, new_product, new_cost, new_quantity)
        shoe_obj.append(new_shoe)

        inventory_write.write(f'\n{new_country},{new_code},{new_product},{new_cost},{new_quantity}')
        print("\n       New stock captured successfully.\n")
        inventory_write.close()

    except FileNotFoundError as error:
        print("\n       Error messagae:  File not found\n")
        print(error)

    finally:
        if file is not None:
            file.close()

#__________________________________#view_all
def view_all():

    file = None
    
    try:
        print("\n                        Inventory Control Sheet\n")
        country = []
        code = []
        product = []
        cost = []
        table  = []
        quantity = []

        for lines in shoe_obj:
            country.append(lines.get_country())
            code.append(lines.get_code())
            product.append(lines.get_product())
            cost.append(lines.get_cost())
            quantity.append(lines.get_quantity())
        table = zip(country, code, product, cost, quantity)
        print(tabulate(table, headers = ('Country','Code', 'Product', 'Cost', 'Quantity'), tablefmt='fancy_grid'))
 
    except FileNotFoundError as error:
        print("\n       Error messagae:  File not found\n")
        print(error)

    finally:
        if file is not None:
            file.close()

#___________________________________#re_stock
#indicate low level stock 
#restock
def restock():

    file = None

    restock_list = []
    country = []
    code = []
    product = []
    cost = []
    quantity = []
    table  = []

    try:
        shoe_obj.sort(key=lambda x:x.quantity)

        for i in range(1,6):
            restock_list.append(shoe_obj[i])
    
        print("\n                Choose product to restock from list below:\n")

        for line in restock_list:
            country.append(line.get_country())
            code.append(line.get_code())
            product.append(line.get_product())
            cost.append(line.get_cost())
            quantity.append(line.get_quantity())
        table = zip(country, code, product, cost, quantity)
        print(tabulate(table, headers = ('Country','Code', 'Product', 'Cost', 'Quantity'), tablefmt='fancy_grid', showindex= range(1,6)))
        
        user_input_item = int(input("\nEnter line number of product to be restocked:"))
        user_input_qty = int(input("Enter quantity:"))
        shoe_obj[user_input_item].set_quantity(user_input_qty)

        output = ''
        for item in shoe_obj:
            output += (f'{item.get_country()},{item.get_code()},{item.get_product()},{item.get_cost()},{item.get_quantity()}\n')

        inventory_write_test = open("inventory.txt", "w")
        inventory_write_test.write(output)
        inventory_write_test.close()
        print("\nNew product information captured.")

    except FileNotFoundError as error:
        print("\n       Error messagae:  File not found\n")
        print(error)

    finally:
        if file is not None:
            file.close()

#___________________________________#search_shoe
def search_shoe():
    code = input("Enter shoe code to search: ")
    for shoe in shoe_obj:
        if shoe.get_code() == code:
            print(f'{shoe.get_code()}.{shoe.get_country()},{shoe.get_product()},{shoe.get_cost()},{shoe.get_quantity()}\n')
            return
    print("Shoe not found.")

#___________________________________#value of shoes
def value_per_item():

    for line in shoe_obj:
        value = int(line.get_cost()) * int(line.get_quantity())
        print(f'{line.get_code()} Value in ZAR: {value}\n')

#___________________________________#overstocked shoes
def highest_quantity():

    highest_qty = []

    for line in shoe_obj:
        highest_qty.append(line)

    print("\nOverstocked product/s marked for sale:\n")
    print(max(shoe_obj, key=lambda item: item.quantity))
    print("Select new option from the menu. ")

#__________________________________________________________________________________________
#menu list
read_shoes_data()
while True:

    try:
        menu = int(input('''\n
            NIWIS - Nike International Warehousing Inventory System\n 
                     Select option from the menu below:\n
            1. Capture new products
            2. Inventory Control Sheet for all products
            3. Restock low product levels  
            4. Search for product
            5. Monetary value of products
            6. For sale items
            \nEnter option:'''))

        if menu == 1:
            capture_shoes()
        elif menu == 2:
            view_all()
        elif menu == 3:
             restock()
        elif menu == 4:
            search_shoe()
        elif menu == 5:
            value_per_item()
        elif menu == 6:
            highest_quantity()
              
    except ValueError:
        print("\n       Invalid selection. Select option from the menu.\n")
        
