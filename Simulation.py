from random import randint			# For Random Generation of Population
from Person import Person 			# Person Class for population
import Market 						# Market File is similar to config file
import matplotlib.pyplot as plt 	# For plotting results and analysis
import csv 							# For exporting data as CSV File

# Simultation Class generates a random population with mainly three type.
# Highly Rich, Rich and Medium Class.

class Simulation:

	def __init__(self, pop_size):
		self.population = []
		self.pop_size = pop_size						# initial population size

	# This method generates a random population.
	def generatePopulation(self):
		for x in range(1, self.pop_size):
			
			# Creating a person
			typeOfPerson = randint(0,2)					# Type 0 MED, 1 RICH, 2 HIGHLY RICH

			if typeOfPerson == 0:
				willToBuy = float(randint(2,5)/10)		# Will to buy [2,5]
				threshold = float(randint(7,9)/10)		# Threshold   [7,9]

			elif typeOfPerson == 1:
				willToBuy = float(randint(4,7)/10)		# Will to buy [4,7]
				threshold = float(randint(6,7)/10)		# Threshold   [7,9]

			elif typeOfPerson == 2:
				willToBuy = float(randint(7,9)/10)		# Will to buy [7,9]
				threshold = float(randint(5,6)/10)		# Threshold   [7,9]

			p = Person(typeOfPerson, willToBuy, threshold)
			self.population.extend([p])


	# This method is main simulation method.
	def playSimulation(self):
		start = 0;

		# This is the year loop.
		for k in range(1, 4):

			# Prints the production limit of that particular year
			print("Production per day limit: "+str(Market.production_limit_per_day))

			# This is the days loop
			for i in range(1, 365):

				# Per day sales and call in for repairs
				print("Year: "+str(k)+" | Day: "+str(i))

				# Selling products to only limit set in Market file.
				for j in range(0, Market.production_limit_per_day-1):
					self.population[start + j].buyProduct()	# This statement calls the buy method of the population class.

				# This variable allows other population to buy product.
				start += Market.production_limit_per_day

				# Circle back to the start of population.
				if(start >= self.pop_size):
					start = 0
					break

				# This method takes into account of the faulty products and their repair cost as well as alters the populatrity of the product.
				Market.callRepair()

				# This method generates results day wise.
				Market.GenerateResultsPerDay(len(Market.person_product)-1)

			# Increasing per day production limit every year
			Market.production_limit_per_day += k*15
			Market.ad_sponsor_amount += k*1000


	# This method plots the results after simulation in order to analyse the result.
	def showResults(self):
		f, axarr = plt.subplots(1, 2, sharey=True)

		# Airhelm was the Placeholder company name
		f.suptitle('AirHelm Profit Projection Chart')

		axarr[0].plot(Market.y)
		axarr[0].plot([0 for x in range(len(Market.y))])
		axarr[0].set_xlabel("Product Sold")
		axarr[0].set_ylabel("Total Profit")
		
		axarr[1].scatter(365, Market.total_revenue_per_day[365], c='r', marker='o')
		axarr[1].scatter(730, Market.total_revenue_per_day[730], c='r', marker='o')
		axarr[1].plot(Market.total_revenue_per_day)
		axarr[1].plot([0 for x in range(len(Market.total_revenue_per_day))])
		axarr[1].set_xlabel("Day(s)")
		axarr[1].set_ylabel("Total Profit")

		plt.show()

	def showResultsPerProduct(self):
		plt.plot(Market.y)
		plt.title("Total Profit vs Product Sold")
		plt.xlabel("Product Sold")
		plt.ylabel("Total Profit")
		plt.show()

	def showProductPerson(self):
		Market.showProductPerson()

	def showResultsPerDay(self):
		plt.plot(Market.total_revenue_per_day)
		plt.title("Total Profit vs Days")
		plt.xlabel("Day(s)")
		plt.ylabel("Total Profit")
		plt.show()

	# This method Exports all the data as CSV file for further processing.
	def exportAllData(self):
		with open("csv/per_product.csv","w") as f:
			wr = csv.writer(f, delimiter="\n")
			wr.writerow(Market.y)

		with open("csv/per_day.csv","w") as f:
			wr = csv.writer(f, delimiter="\n")
			wr.writerow(Market.total_revenue_per_day)