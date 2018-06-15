# Product Class contains the Total manufacturing cost of the product, profit gained on that piece of the product.
# Total cost will be calculated using these variables.
# isFailed variable gives us the info on whether the Product piece is faulty or not. If yes or true then repair will be Called

class Product:

	def __init__(self, total_cost, profit, isFailed):
		self.total_cost = total_cost
		self.profit = profit
		self.isFailed = isFailed