# Sales Management 
"""
This program creates a RetailManagement class, which keeps track of products, customers, and sales. 
The class has methods to add products, customers, and sales, as well as methods to generate reports on sales, 
products, and customers. The program also includes classes for Product, Customer, and Sale, which store information 
about each of those entities. An example of usage is provided at the bottom of the program, where two products 
and two customers are added, two sales are made, and the reports are generated."""

class RetailManagement:
    def __init__(self):
        self.products = []
        self.customers = []
        self.sales = []
    
    def add_product(self, product):
        self.products.append(product)
    
    def add_customer(self, customer):
        self.customers.append(customer)
    
    def make_sale(self, sale):
        self.sales.append(sale)
        
    def get_sales_report(self):
        total_sales = 0
        for sale in self.sales:
            total_sales += sale.amount
        print("Total Sales: ", total_sales)
        
    def get_product_report(self):
        for product in self.products:
            print("Product: ", product.name)
            print("Stock: ", product.stock)
            print("Price: ", product.price)
            
    def get_customer_report(self):
        for customer in self.customers:
            print("Customer: ", customer.name)
            print("Phone: ", customer.phone)
            print("Address: ", customer.address)

class Product:
    def __init__(self, name, stock, price):
        self.name = name
        self.stock = stock
        self.price = price

class Customer:
    def __init__(self, name, phone, address):
        self.name = name
        self.phone = phone
        self.address = address

class Sale:
    def __init__(self, product, customer, amount):
        self.product = product
        self.customer = customer
        self.amount = amount

"""
Example usage
rm = RetailManagement()

product1 = Product("Shampoo", 50, 10)
product2 = Product("Conditioner", 40, 15)

customer1 = Customer("John Smith", "555-555-5555", "123 Main St")
customer2 = Customer("Jane Doe", "555-555-5556", "456 Park Ave")

rm.add_product(product1)
rm.add_product(product2)

rm.add_customer(customer1)
rm.add_customer(customer2)

sale1 = Sale(product1, customer1, 15)
sale2 = Sale(product2, customer2, 20)

rm.make_sale(sale1)
rm.make_sale(sale2)

rm.get_sales_report()
rm.get_product_report()
rm.get_customer_report()
"""
