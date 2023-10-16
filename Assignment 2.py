# 

class product:
    def __init__(self, code, name, sale_price, manufacture_cost, stock_level, estimated_units_manufactured)
        self.code = code
        self.name = name
        self.sale_price = sale_price
        self.manufacture_cost = manufacture_cost
        self.stock_level = stock_level
        self.esitmated_units_manufactured = estimated_units_manufactured

# create simulation of monthly sales 

    def simulate_monthly_sales(self, months):
        for _ in range(months):
            units_manufactured = self.estimated_units_manufactured
            units_sold = random.randint(units_manufactured - 10, units_manufactured + 10)
            self.stock_level += units_manufactured - units_sold
            self.monthly_stock.append(self.stock_level)
            profit_or_loss = (units_sold * self.sale_price) - (units_manufactured * self.manufacture_cost)
            self.monthly_profit.append(profit_or_loss) 



