from random import randint
from Product import Product
import Market

class Person:

	def __init__(self, typeOfPop, willToBuy, threshold):
		self.typeOfPop = typeOfPop
		self.willToBuy = willToBuy
		self.threshold = threshold
		self.hasBought = 0

	def buyProduct(self):

		# Generating Situation
		mood = float(0.3*Market.product_popularity) + float(0.7*self.willToBuy/(self.hasBought+1))

		# RICH people can buy multiple
		if self.typeOfPop != 0:
			if mood >= self.threshold:
				Market.product_sold += 1
				self.hasBought += 1

				# creating product instance
				fail = not bool(randint(0,500)%500)
				pr = Product(Market.total_cost_per_product, Market.profit_per_product, fail)

				# Adding info to Market
				Market.person_product.append([pr, self])

				# Updating Market Status
				Market.updateMarketStatus()

		# MED type person only buys one
		else:
			if mood >= self.threshold and self.hasBought == 0:
				Market.product_sold += 1
				self.hasBought += 1

				# creating product instance
				fail = not bool(randint(0,500)%500)
				if Market.product_sold > Market.rate_product_sold and Market.product_popularity > 0.6:

					# if one year is crossed and product has become popular
					pr = Product(Market.total_cost_per_product*Market.GAIN_FACTOR, Market.profit_per_product*Market.GAIN_FACTOR, fail)

				else:
					pr = Product(Market.total_cost_per_product, Market.profit_per_product, fail)

				# Adding info to Market
				Market.person_product.append([pr, self])

				# Updating Market Status
				Market.updateMarketStatus()