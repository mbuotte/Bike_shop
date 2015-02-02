from bicycles import Bicycle, BikeShop, Customer

def main():
    bikeOne = Bicycle("Comfort", 20, 800)
    bikeTwo = Bicycle("Urban", 40, 550)
    bikeThree = Bicycle("Mountain", 35, 550)
    bikeFour = Bicycle("Road", 20, 400)
    bikeFive = Bicycle("Electric", 44, 150)
    bikeSix = Bicycle("Hybrid", 38, 900)
    
    inventory_list = [
        bikeOne, bikeTwo, bikeThree, bikeFour, bikeFive, bikeSix
    ]
    sold_list = []
    shopOne = BikeShop ("ACME Bikes", inventory_list, sold_list)
    
    customerOne = Customer("Joe Smith",200)
    customerTwo = Customer ("Jane Doe", 500)
    customerThree = Customer ("Ed Jones", 1000)
    
    customer_list = [
      customerOne, customerTwo, customerThree
    ]
    
    # Print the bikes each customer can afford
    for customer in range(len(customer_list)):
      print '-' * 20
      for bike in range(len(inventory_list)):
        if customer_list[customer].funds > inventory_list[bike].cost:
            print "{0} can afford the {1}".format(
                    customer_list[customer].customer_name,
                    inventory_list[bike].model_name
            )
    print '-' * 80
    
    # Print the initial inventory of the bike shop
    print "{0} Bike Shop carries: ".format(shopOne.shop_name)
    for item in range(len(shopOne.inventory)):
      print "Model: {0}   Cost: {1}".format (shopOne.inventory[item].model_name,shopOne.inventory[item].cost)    
   
    print '-' * 80

    # Have each customer buy a bike and show the funds they have left after the purchase
    for customer in range(len(customer_list)):
      for bike in range(len(inventory_list)):  
        if customer_list[customer].funds > inventory_list[bike].cost:
          print "Customer: {0}   Has enough funds: {1}   to cover Cost: {2}".format(customer_list[customer].customer_name, customer_list[customer].funds, inventory_list[bike].cost)
          customer_list[customer].buy_bike(inventory_list[bike])
          print "    After buying: {0} Customer: {1}  Has: {2} Left".format(inventory_list[bike].model_name, customer_list[customer].customer_name,  customer_list[customer].funds)
          shopOne.sell_bike(inventory_list[bike].model_name)
          break
    print '-' * 80

    # Print the total sales for the Bike Shop
    print "{0} Bike Shop total sales: ".format(shopOne.shop_name)
    profit=0
    for current in shopOne.sold:
      print current.model_name, current.cost
      profit+=current.cost*.2
    print "For a total profit of {0}".format(profit)
    print '-' * 80

      
if __name__ == "__main__":
    main()
    

