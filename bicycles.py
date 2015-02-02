class Bicycle (object):
    """
    Bicycles have a model name, a weight, and a cost to produce.
    """
  
    def __init__(self, model_name, weight, cost):
        self.model_name = model_name
        self.weight = weight
        self.cost = cost
        
    def _repr_(self):
        return "{0} weighs {1} pounds and costs ${2} to produce.".format(self.model_name, self.weight, self.cost)

    def changeName (self, model_name):
        self.model_name = model_name

    def changeCost (self, cost):
        self.cost = cost

    def changeWeight (self, weight):
        self.weight = weight

# ------------------------------------------------------------------------
class BikeShop(object):
    """
    Bike Shops have a name and an inventory.
    """
    def __init__(self, shop_name, inventory, sold):
        self.shop_name = shop_name
        self.inventory = inventory
        self.sold = sold
    def _repr_ (self):
      return "{0} Bike Shop carries: {1}".format(self.shop_name, self.inventory)

    def sell_bike(self,model):
      for bike in range(len(self.inventory)):
        if str(self.inventory[bike].model_name) == str(model):
          self.sold.append(self.inventory[bike])
          break
      return self.inventory[bike].model_name

    def get_price (self,model):
      for bike in range(len(self.inventory)):
        if str(self.inventory[bike].model_name) == str(model):
          return (self.inventory[bike].cost)
          break
      return (-1)
          
        

# ------------------------------------------------------------------------
class Customer(object):
    """
    Customers have a name and fund of money.
    """
    def __init__(self, customer_name, funds):
        self.customer_name = customer_name
        self.funds = funds

    def _repr_ (self):
        return "{0} has ${1}.".format(self.customer_name, self.funds)
      
    def buy_bike (self, Bike):
      self.funds = self.funds - Bike.cost
