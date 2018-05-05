from Simulation import Simulation

s1 = Simulation(50000)
s1.generatePopulation()
s1.playSimulation()

# Exporting Data
s1.exportAllData()

s1.showResults()
# s1.showResultsPerDay()
# s1.showResultsPerProduct()
# s1.showProductPerson()

print("DONE!")