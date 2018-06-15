from Simulation import Simulation 		# This class contains the major methods required.

# Arguement carries population size
s1 = Simulation(100000)					# This initiated the variable for population size.
s1.generatePopulation()					# This generates the population as per the desired size.
s1.playSimulation()						# This method runs the simulation and populates the arrays with data.

# Exporting Data
# s1.exportAllData()					# This Method exports the data as CSV file.

s1.showResults()						# This Method shows the plot of entire day wise and sales wise projection.
# s1.showResultsPerDay()				# This method only shows the day wise results.
# s1.showResultsPerProduct()			# This method only shows the sales wise results.

print("DONE!")							# Prints done at the end giving a successful run indication.