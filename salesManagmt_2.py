# Sales Management Program in Python

class SalesManagement:
    def __init__(self):
        self.sales = []
    
    def add_sale(self, sale):
        self.sales.append(sale)
    
    def remove_sale(self, sale):
        self.sales.remove(sale)
    
    def total_sales(self):
        total = 0
        for sale in self.sales:
            total += sale.amount
        return total
    
    def top_performing_salesperson(self):
        top_salesperson = None
        top_sales = 0
        for sale in self.sales:
            if sale.salesperson.sales > top_sales:
                top_sales = sale.salesperson.sales
                top_salesperson = sale.salesperson
        return top_salesperson
    
    def sales_by_region(self, region):
        region_sales = 0
        for sale in self.sales:
            if sale.region == region:
                region_sales += sale.amount
        return region_sales
    
class Sale:
    def __init__(self, salesperson, amount, region):
        self.salesperson = salesperson
        self.amount = amount
        self.region = region

class Salesperson:
    def __init__(self, name, sales=0):
        self.name = name
        self.sales = sales
    
    def add_sale(self, amount):
        self.sales += amount

# Example of usage

sales_manager = SalesManagement()

salesperson1 = Salesperson("John Smith")
salesperson2 = Salesperson("Jane Doe")

sale1 = Sale(salesperson1, 1000, "East Coast")
sale2 = Sale(salesperson1, 500, "West Coast")
sale3 = Sale(salesperson2, 1500, "West Coast")

sales_manager.add_sale(sale1)
sales_manager.add_sale(sale2)
sales_manager.add_sale(sale3)

print("Total Sales:", sales_manager.total_sales())

# Output: Total Sales: 2500
print("Top Performing Salesperson:", sales_manager.top_performing_salesperson().name)

# Output: Top Performing Salesperson: Jane Doe
print("Sales by Region (West Coast):", sales_manager.sales_by_region("West Coast"))


