# Products supply chain Management 


class SupplyChain:
    def __init__(self):
        self.suppliers = []
        self.warehouses = []
        self.retailers = []
        
    def add_supplier(self, supplier):
        self.suppliers.append(supplier)
        
    def add_warehouse(self, warehouse):
        self.warehouses.append(warehouse)
        
    def add_retailer(self, retailer):
        self.retailers.append(retailer)
        
    def order_from_supplier(self, supplier_name, product, quantity):
        for supplier in self.suppliers:
            if supplier.name == supplier_name:
                supplier.place_order(product, quantity)
                break
                
    def receive_from_supplier(self, supplier_name, product, quantity):
        for supplier in self.suppliers:
            if supplier.name == supplier_name:
                supplier.deliver(product, quantity)
                break
                
    def distribute_to_warehouses(self, product, quantity):
        for warehouse in self.warehouses:
            warehouse.receive(product, quantity)
            
    def sell_to_retailer(self, warehouse_name, product, quantity):
        for warehouse in self.warehouses:
            if warehouse.name == warehouse_name:
                warehouse.sell(product, quantity)
                break
                
    def purchase_from_retailer(self, retailer_name, product, quantity):
        for retailer in self.retailers:
            if retailer.name == retailer_name:
                retailer.purchase(product, quantity)
                break
                
    def check_inventory(self, warehouse_name):
        for warehouse in self.warehouses:
            if warehouse.name == warehouse_name:
                return warehouse.inventory
                
    def check_sales(self, retailer_name):
        for retailer in self.retailers:
            if retailer.name == retailer_name:
                return retailer.sales
                

class Supplier:
    def __init__(self, name):
        self.name = name
        self.inventory = {}
        
    def place_order(self, product, quantity):
        self.inventory[product] += quantity
        
    def deliver(self, product, quantity):
        self.inventory[product] -= quantity
        
    def check_inventory(self):
        return self.inventory
        

class Warehouse:
    def __init__(self, name):
        self.name = name
        self.inventory = {}
        
    def receive(self, product, quantity):
        self.inventory[product] += quantity
        
    def sell(self, product, quantity):
        self.inventory[product] -= quantity
        
    def check_inventory(self):
        return self.inventory
        

class Retailer:
    def __init__(self, name):
        self.name = name
        self.sales = {}
        
    def purchase(self, product, quantity):
        self.sales[product] += quantity
        
    def check_sales(self):
        return self.sales
        
        
