from Simulation import Simulation

# Arguement carries population size
s1 = Simulation(100000)
s1.generatePopulation()
s1.playSimulation()

# Exporting Data
# s1.exportAllData()

s1.showResults()
# s1.showResultsPerDay()
# s1.showResultsPerProduct()

print("DONE!")