


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

        
