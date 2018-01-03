import os
import yieldiv as yield_mod
import stockpps as stockpps_mod


def display_menu():
    os.system('clear')
    print("Gather Stock Yield or Price-per-Share")
    u_choice = input('Input "d" in order to Compute Dividend Yield OR "p" for the Price-Per-Share: ')
    u_choice = u_choice.lower()

    if u_choice == "d":
        compute_div()
    elif u_choice == 'p':
        compute_pps()
    else:
        print('\nPlease insert a valid character.  Input only accepts "d" or "p"')
        exit(1)


def compute_div():
    stockprice = float(input("Stock Price at time of purchase:\t"))
    passprice = yield_mod.compute_yield(stockprice)
    print("Debug Stock Price: ", passprice)
    print("Debug Div Total:", )


def compute_pps():
    stockprice = float(input("Stock Price at time of purchase:\t"))
    value = stockpps_mod.stockpps(stockprice)
    print("What is this value: ", value)
    print("Debug: compute_pps completed")


def main():
    choice = "y"
    while choice.lower() == "y":
        display_menu()
        print("Did this work?")
        print("\n")
        choice = input('Do you wish to continue (y/n): ')
        choice = choice.lower()
        print("\n")


print("Closing")

if __name__ == "__main__":
    main()


exit(0)
