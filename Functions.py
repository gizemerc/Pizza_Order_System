import csv
from tabulate import tabulate
import datetime
import Pizza as pz



#Show menu, read from Menu.txt file
def show_menu():
    menu_open=open("Menu.txt","r")
    print("\n----------------MENU----------------")
    print(menu_open.read())
    print("--------------------------------\n")

#Choose a pizza from the menu. If choice is not in the list ask again
def choose_pizza():
    pizza_choice=input("Which pizza do you want to choose?")
    if pizza_choice == "Classic":
        PizzaCS = pz.Classic()
    elif pizza_choice == "Margherita":
        PizzaCS = pz.Margarita()
    elif pizza_choice == "TurkPizza":
        PizzaCS = pz.Turk_Pizza()
    elif pizza_choice == "PlainPizza":
        PizzaCS = pz.Plain()
    else:
        print("----------------\n!!!Please choose a pizza from the list!!!\n--------------------")
        pizza_choice,PizzaCS = choose_pizza()
    return pizza_choice,PizzaCS

#Choose a sauce from the menu. If choice is not in the list ask again
def choose_sauce():
    sauce_choice=input("Which sauce do you want to choose?")
    if sauce_choice == "Olives":
        SauceCS = pz.Olives()
    elif sauce_choice == "Mushrooms":
        SauceCS = pz.Mushrooms()
    elif sauce_choice == "GoatCheese":
        SauceCS = pz.Goat_Cheese()
    elif sauce_choice == "Meat":
        SauceCS = pz.Meat()
    elif sauce_choice == "Onions":
        SauceCS = pz.Onions()
    elif sauce_choice == "Corn":
        SauceCS = pz.Corn()
    else:
        print("----------------\n!!!Please choose a sauce from the list!!!\n----------------")
        sauce_choice,  SauceCS =choose_sauce()
    return sauce_choice, SauceCS

#Show preferences and total price
def show_order(PizzaCS,SauceCS):
    Order_Total=pz.Decorator(PizzaCS,SauceCS)
    Order_Description=Order_Total.get_description()
    print("\n---------------------ORDER INFO----------------------------")
    print("Order Description: \n",Order_Description)
    Total_Price=Order_Total.get_cost()
    print("Total Price: ",Total_Price)
    return Order_Description,Total_Price

#Ask payment information and record it
def pay_info(pizza_choice, sauce_choice,Total_Price):
    print("\n---------------------PAYMENT INFO----------------------------")
    name=input("Please enter your name:")
    ID_number=input("Please enter your ID number:")
    credit_card_number=input("Please enter your credit card number:")
    credit_card_password=input("Please enter your credit card password:")
    order_date=datetime.datetime.now()
    create_file()
    order_data = [order_date, name, ID_number, credit_card_number, credit_card_password, pizza_choice, sauce_choice,Total_Price]
    file = open('Orders_Database.csv', 'a')
    writer = csv.writer(file)
    writer.writerow(order_data)
    file.close()

#Control if a file exists
def create_file():
    try:
        file=open('Orders_Database.csv', 'x')
        header=["Order Date","Name","ID","Credit Card Number","Credit Card Password", "Pizza Choice","Sauce Choice","Total Price"]
        writer = csv.writer(file)
        writer.writerow(header)
        file.close()
    except:
        print("File exist!!")

#Show order list
def show_order_list():
    print("\n---------------------ORDER LIST----------------------------")
    rows = []
    file=open("Orders_Database.csv")
    read_file = csv.reader(file)
    for row in read_file:
        rows.append(row)
    print(tabulate(rows))

