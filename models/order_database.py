from models.order import *

order_01 = Order("Bob Baxter", "25/03/2023", "Brilliant Burgers", "B. Urgha", 3)
order_02 = Order("Annie Ant", "27/03/2023", "Always Available Antiques", "Anne Tique", 1)
order_03 = Order("Calvin Cooke", "28/03/2023", "Colourful Collections", "Cobalt Chesterton", 1)

orders = [order_01, order_02, order_03]

# from solution ---> date/time format

# from models.order import *
# import datetime

# order1 = Order(datetime.date(2020, 5, 17), "Luke Skywalker", 1,  'Pepperoni')
# order2 = Order(datetime.date(2020, 6, 18), "Han Solo", 2, "Quatro Fromagio")
# order3 = Order(datetime.date(2020, 7, 19), "Darth Vader", 1, "Pineapple")

# orders = [order1, order2, order3]