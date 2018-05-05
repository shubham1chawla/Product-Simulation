from random import randint
from Person import Person
import Market
import matplotlib.pyplot as plt

class Simulation:

	def __init__(self, pop_size):
		self.population = []
		self.pop_size = pop_size					# initial population size

	def generatePopulation(self):
		for x in range(1, self.pop_size):
			
			# Creating a person
			typeOfPerson = randint(0,2)				# Type 0 MED, 1 RICH, 2 HIGHLY RICH

			if typeOfPerson == 0:
				willToBuy = float(randint(2,5)/10)
				threshold = float(randint(7,9)/10)

			elif typeOfPerson == 1:
				willToBuy = float(randint(4,7)/10)
				threshold = float(randint(6,7)/10)

			elif typeOfPerson == 2:
				willToBuy = float(randint(7,9)/10)
				threshold = float(randint(5,6)/10)

			p = Person(typeOfPerson, willToBuy, threshold)
			self.population.extend([p])


	def playSimulation(self):
		start = 0;

		for k in range(1, 4):
			for i in range(1, 365):

				# Per day sales and call in for repairs
				print("Year: "+str(k)+" | Day: "+str(i))

				# Selling products
				for j in range(0, Market.production_limit_per_day-1):
					self.population[start + j].buyProduct()

				start += Market.production_limit_per_day
				if(start >= self.pop_size):
					break
				Market.callRepair()

			# Increasing per day production limit every year
			Market.production_limit_per_day += k*15


	def showResults(self):
		plt.plot(Market.y)
		plt.show()


	def showProductPerson(self):
		Market.showProductPerson()