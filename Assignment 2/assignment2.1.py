


class Product:
    def __init__(self, code, name, sale_price, manufacture_cost, stock_level, estimated_units_manufactured):
        self.code = code
        self.name = name
        self.sale_price = sale_price
        self.manufacture_cost = manufacture_cost
        self.stock_level = stock_level
        self.estimated_units_manufactured = estimated_units_manufactured
        self.monthly_stock = [stock_level]
        self.monthly_profit = []

    def simulate_monthly_sales(self, months):
        month = 1
        units_manufactured = self.estimated_units_manufactured
        while month <= months:
            units_sold = random.randint(units_manufactured - 10, units_manufactured + 10)
            self.stock_level += units_manufactured - units_sold
            self.monthly_stock.append(self.stock_level)
            profit_or_loss = (units_sold * self.sale_price) - (units_manufactured * self.manufacture_cost)
            self.monthly_profit.append(profit_or_loss)
            month += 1


    def generate_stock_statement(self):
        print("Product Code: " + str(self.code))
        print("Product Name: " + self.name)
        print("Sale Price: $" + str(self.sale_price))
        print("Manufacture Cost: $" + str(self.manufacture_cost))
        print("Initial Stock Level: " + str(self.monthly_stock[0]) + " units")
        print("Predicted Monthly Stock:")

        month = 1
        for stock, profit in zip(self.monthly_stock[1:], self.monthly_profit):
            print("Month " + str(month) + ": Stock: " + str(stock) + " units, Profit/Loss: $" + "{:.2f}".format(profit))
            month += 1

    def get_positive_integer(prompt):
         value = int(input(prompt))
         return value

    def get_positive_float(prompt):
          value = float(input(prompt))
          return value
    

    def entry_point():

        code = get_positive_integer("Enter the product code (between 100 and 1000): ")
        name = input("Product Name (e.g., Laser Printer): ")
        sale_price = get_positive_float("Product Sale Price (greater than zero): $")
        manufacture_cost = get_positive_float("Product Manufacture Cost (greater than zero): $")
        stock_level = get_positive_integer("Initial Stock Level (greater than 0): ")
        estimated_units_manufactured = get_positive_integer("Estimated Monthly Units Manufactured (0 or greater): ")
        months = 12

        product = Product(code, name, sale_price, manufacture_cost, stock_level, estimated_units_manufactured)
        product.simulate_monthly_sales(months)
        product.generate_stock_statement()

        total_units_sold = sum(product.monthly_profit)
        total_units_manufactured = sum(product.estimated_units_manufactured for _ in range(months))
        net_profit = total_units_sold * sale_price - total_units_manufactured * manufacture_cost 

    
        
    
    


