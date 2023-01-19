# Retail Store Management 
"""
This program creates a RetailStore class that can be used to manage the inventory of a store. 
The class has methods for checking the current inventory, adding items to the inventory, 
removing items from the inventory, and updating the price of an item. 
The program also includes example usage of the class to add, remove, and update items in the store's inventory.
"""

class RetailStore:
    def __init__(self, name, inventory):
        self.name = name
        self.inventory = inventory
    
    def check_inventory(self):
        for item in self.inventory:
            print(f'{item["name"]} - Quantity: {item["quantity"]} - Price: ${item["price"]}')
    
    def add_to_inventory(self, item_name, quantity, price):
        self.inventory.append({"name": item_name, "quantity": quantity, "price": price})
        print(f'{quantity} units of {item_name} have been added to the inventory at ${price} each.')
    
    def remove_from_inventory(self, item_name, quantity):
        for item in self.inventory:
            if item["name"] == item_name:
                if item["quantity"] < quantity:
                    print(f'Error: Not enough units in stock to remove {quantity} of {item_name}.')
                else:
                    item["quantity"] -= quantity
                    print(f'{quantity} units of {item_name} have been removed from the inventory.')
                    break
    
    def update_price(self, item_name, new_price):
        for item in self.inventory:
            if item["name"] == item_name:
                item["price"] = new_price
                print(f'The price of {item_name} has been updated to ${new_price}.')
                break


"""
# Initialize store with some inventory
store = RetailStore("My Store", [{"name": "Shirt", "quantity": 10, "price": 20}, {"name": "Pants", "quantity": 5, "price": 30}])

# Check current inventory
store.check_inventory()

# Add more items to inventory
store.add_to_inventory("Socks", 12, 5)
store.add_to_inventory("Hat", 8, 15)

# Check updated inventory
store.check_inventory()

# Remove items from inventory
store.remove_from_inventory("Shirt", 5)
store.remove_from_inventory("Pants", 10)

# Check inventory again
store.check_inventory()

# Update price of an item
store.update_price("Socks", 4)

# Check final inventory
store.check_inventory()
"""