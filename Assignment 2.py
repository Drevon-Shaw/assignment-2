#create a product class and initilize 
class product:
    def __init__(self, code, name, sale_price, manufacture_cost, stock_level, estimated_units_manufactured):
        self.code = code
        self.name = name
        self.sale_price = sale_price
        self.manufacture_cost = manufacture_cost
        self.stock_level = stock_level
        self.estimated_units_manufactured = estimated_units_manufactured
        self.monthly_stock = [stock_level]
        self.monthly_profit = []
        