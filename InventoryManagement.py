# Products inventory Management 


class InventoryManagement:
    def __init__(self):
        self.items = {}
        
    def add_item(self, item, quantity):
        if item in self.items:
            self.items[item] += quantity
        else:
            self.items[item] = quantity
            
    def remove_item(self, item, quantity):
        if item in self.items:
            if self.items[item] >= quantity:
                self.items[item] -= quantity
            else:
                raise ValueError("Not enough of this item in stock.")
        else:
            raise ValueError("This item is not in the inventory.")
