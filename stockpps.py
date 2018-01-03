def stockpps(stockprice):
    print("Debug stockprice: ", stockprice)
    totalshares = float(input("How many shares were purchased: "))
    print('Debug Total Amount: {:.2f}'.format(totalshares))
    compute_totcost = float(totalshares * stockprice)
    print("Debug Total Cost: ${:,.2f}".format(compute_totcost))
    compute_pps = float(compute_totcost / totalshares)
    print("Debug PPS:", compute_pps)
