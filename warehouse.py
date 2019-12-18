# single line comments

""" 
Program: Warehouse inventory control system
Functionality: Warehouse
    - Register new items 
        id(auto generated)
        title
        category
        price
        quantity on stock
    -Print items with no Stock
    -Update the stock with
    -Remove items 

    -Print different categories 
    -Print Stock Value (sum (price * stock))

    - Register Purchase
    -Register sell 

    -Log of events
        time | action | itemId

        1 - generate log str inside important functions
        2- add that str to logs array
        3 - save logs array to
        4 - load logs array when system starts



"""

from menu import print_menu
from item import Item
import datetime
import pickle


items = []
logs = []
id_count = 1
items_file = "item.data"
logs_file = "logs.data"


def get_time():
    current_date = datetime.datetime.now()
    time = current_date.strftime("%X")
    return time

def save_items():
    #open creastes / opens a file
    writer = open(items_file, "wb") #wb = write binary 
    pickle.dump(items, writer) # converts the object into binary and writes it on the file 
    writer.close() #closes the file stream (to release the file)
    print(" Data Saved!!")

def save_log():
    #open creastes / opens a file
    writer = open(logs_file, "wb") #wb = write binary 
    pickle.dump(logs, writer) # converts the object into binary and writes it on the file 
    writer.close() #closes the file stream (to release the file)
    print(" Log Saved!!")

def read_items():
    global id_count #import variable into fn scope

    try:
        reader = open(items_file, "rb") #rb = read binary 
        temp_list = pickle.load(reader) #read the binary and convert it to the original object
            
        for item in temp_list:
            items.append(item)
        
        last = items[-1]
        id_count = last.id + 1
        print("Loaded: " + str(len(temp_list)) + " items ")
    except: 
        #you get here if try block crashes 
        print(" *Error: Data could not be loaded! ")

def read_log():
    try:
        reader = open(logs_file, "rb") #rb = read binary 
        temp_list = pickle.load(reader) #read the binary and convert it to the original object
            
        for log in temp_list:
            logs.append(log)
        
        print("Loaded: " + str(len(temp_list)) + " log events ")
    except: 
        #you get here if try block crashes 
        print(" *Error: Data could not be loaded! ")

def print_header(text):
    print("\n\n")
    print("*" * 40)
    print(text)
    print("*" * 40)

def print_all(header_text):
    print_header(header_text)
    print("-" * 90)
    print("ID  | Item Title                | Category        | Price     | Stock      | Stock Value")
    print("-" * 90)
    for item in items: 
        print(str(item.id).ljust(3) + " | " + item.title.ljust(25) + " | " + item.category.ljust(15) + " | " + str(item.price).rjust(9) + " | " + str(item.stock).rjust(6))

def register_item(): 
    global id_count #importing the global variable, into function scope

    print_header(" Register new Item")
    title = input("Please input the Title: ")
    category = input("Please input the Category: ")
    price= float(input("Please input the Price:"))
    stock = int(input("Please input the Stock: "))

    #validations 
    new_item = Item()
    new_item.id = id_count
    id_count += 1
    new_item.title = title
    new_item.category = category
    new_item.price = price
    new_item.stock = stock

    items.append(new_item)
    print(" Item Created! ")

        # #add registery to the logs
        # log_line = get_time() + " | Updated ID: | " + id
        # logs.append(log_line)
        # save_log()


def update_stock():
    #show the user all the items 
    #ask for the desired id
    #get the element from the array with that id
    #ask for the new stock
    #update the stock of the element 

    print_all("Choose an Item from the list ")
    id = input("\nSelect an ID to update its stock: ")

    found = False
    for item in items:
        if(str(item.id) == id):
             stock = input("Please input new stock value: ")
             item.stock = int(stock)
             found = True

             #add registery to the logs
             log_line = get_time() + " | Updated ID: | " + id
             logs.append(log_line)
             save_log()

    if(not found): 
        print("** Error, ID does not exist, try again!")

def remove_item():
    print_all("Choose an Item from the list to remove ")
    id = input("\nSelect an ID to remove from stock: ")

    for item in items:
        if(str(item.id) == id):
            items.remove(item)
            print(" Item has been removed")
            
    #add registery to the logs
    log_line = get_time() + " | Updated ID: | " + id
    logs.append(log_line)
    save_log()

def list_no_stock():
    print_header("Items with no stock")
    for item in items:
        if(item.stock == 0):
            print(item.title)

def print_categories():
    temp_list = []

    for item in items:
        if(item.category not in temp_list):
            temp_list.append(item.category)

    print(temp_list)

def register_purchase():
    
    print_all("Choose an Item from the list ")
    id = input("\nSelect an ID to register the purchase ")
    quantity = int(input("\nSelect quantity of purchase "))

    found = False
    for item in items:
        if(str(item.id) == id):
             stock = input("How many items purchased: ")
             item.stock += int(stock)
             found = True
    
            #add registery to the logs
    log_line = get_time() + " | Updated ID: | " + id
    logs.append(log_line)
    save_log()
    
    if(not found): 
        print("** Error, ID does not exist, try again!")


    """
    Show the items
    ask the user to select an item 
    ask for the quantity in the order (purchase)
    update the stock of the selected item

    """
def register_sell():
    print_all("Choose an Item from the list ")
    id = input("\nSelect an ID to register the sell ")
    quantity = int(input("\nSelect quantity of items sold "))

    found = False
    for item in items:
        if(str(item.id) == id):
             stock = input("How many items sold: ")
             item.stock -= int(stock)
             found = True
    
    #add registery to the logs
    log_line = get_time() + " | Updated ID: | " + id
    logs.append(log_line)
    save_log()
    
    if(not found): 
        print("** Error, ID does not exist, try again! ")

def print_stock_value():
    total = 0.0
    for item in items:
        total += (item.price * item.stock)
    
    print("Total Stock Value: " + str(total))

def print_log(header_text):




#read previous data from the file to items array
    read_items()
    read_log()

opc = ''
while(opc != 'x'):
    print_menu()

    opc = input("Please select an option: ")

    # actions based on selected opc 
    if(opc == "1"):
        register_item()
        save_items()
    elif(opc == "2"):
        print_all("List of all items")
    elif(opc == "3"):
        update_stock()
        save_items()
    elif (opc == "4"):
        list_no_stock()
    elif (opc == "5"):
        remove_item()
        save_items()
    elif(opc == "6"):
        print_categories()
    elif(opc == "7"):
        print_stock_value()
    elif(opc == "8"):
        register_purchase()
        save_items()
    elif(opc == "9"):
        register_sell()
        save_items()
    # elif(opc == "10"):
    #     print_log()

    if(opc != "x"):
        input("\n\nPress Enter to continue...")