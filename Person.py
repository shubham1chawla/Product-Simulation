from random import randint			# Required to create a random mood variable.
from Product import Product 		# Product object is to be created.
import Market 						# Market file contains all the config variables.

class Person:

	def __init__(self, typeOfPop, willToBuy, threshold):
		self.typeOfPop = typeOfPop			# 0 - Medium class people, 1 - Rich People, 2 - Highly Rich.
		self.willToBuy = willToBuy 			# Person's will to buy product, depended on the type of population
		self.threshold = threshold			# Minimum product popularity required to make person buy.
		self.hasBought = 0					# How many product has the perosn bought.

	def buyProduct(self):

		# Generating Situation
		mood = float(0.3*Market.product_popularity) + float(0.7*self.willToBuy/(self.hasBought+1))
		# This is a weighted sum of product popularity, will to buy and whether he has bought the product earlier or not.
		# Will to buy decreases if he has already bought the product significantly.

		# RICH people can buy multiple
		if self.typeOfPop != 0:
			if mood >= self.threshold:
				Market.product_sold += 1
				self.hasBought += 1

				fail = not bool(randint(0,Market.FAULTY_PRODUCT_PROBABILTY)%Market.FAULTY_PRODUCT_PROBABILTY)	# This will initiated a variable that gives a probabilty that product is faulty. (1 in 500)
				pr = Product(Market.total_cost_per_product, Market.profit_per_product, fail)					# creating product instance

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
				fail = not bool(randint(0,Market.FAULTY_PRODUCT_PROBABILTY)%Market.FAULTY_PRODUCT_PROBABILTY)

				# This makes sure that a medium class perosn will only buy the product after product popularity hits a certain level.
				if Market.product_popularity > Market.med_class_pop_threshold:						
					pr = Product(Market.total_cost_per_product, Market.profit_per_product, fail)

				# Adding info to Market
				Market.person_product.append([pr, self])

				# Updating Market Status
				Market.updateMarketStatus()