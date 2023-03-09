import Functions as fn

def main():
    #Print the menu on the screen.
    fn.show_menu()

    #Choose Pizza from the menu
    pizza_choice,PizzaCS=fn.choose_pizza()

    #Choose Sauce from the menu
    sauce_choice, SauceCS=fn.choose_sauce()

    #Show order and total price
    Order_Description,Total_Price=fn.show_order(PizzaCS,SauceCS)


    # Ask payment info and record it (if file is not exist create new one)
    fn.pay_info(pizza_choice, sauce_choice,Total_Price)

    #Show order list
    fn.show_order_list()

if __name__=="__main__":
    main()




