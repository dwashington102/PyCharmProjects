def compute_yield(stockprice):
    print("Debug stockprice: ", stockprice)
    divamount = float(input("What is the dividend amount per share per payout: "))
    yrdist = int(input("How many times per year is the dividend paid: "))
    divtotal = float(divamount * yrdist)
    divyield = ((100 * divtotal) / stockprice)
    print("Total Dividend: {:.2f}".format(divyield)+ '%')



