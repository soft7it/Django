# Main Module : Consumer
from product import *

# p1 = Prpduct('Salad', 100.00)  # __init__()
# p2 = Prpduct('Grape Juice', 50.00)

p1 = createProduct('food', 'Salad', 100.00)  # __init__()
p2 = createProduct('drink', 'Grape Juice', 50.00)

print(p1)  # str(p1)
print(p2)  # str(p2)
