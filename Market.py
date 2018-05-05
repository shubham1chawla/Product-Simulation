import math
from random import randint

total_cost_per_product = 18999		# Initial Per Product Total Cost
profit_per_product = 2000			# Initial Per Product Profit
product_sold = 0					# Number of Product Sold
failed_product = 0					# Number of failed products
rate_product_sold = 4800			# rate of product sold per week
person_product = []
GAIN_FACTOR = 1000					# After every 1000 sold products
product_popularity = 0.216			# Initial Product Popularity
production_limit_per_day = 13;		# Production limit per day for 1st year (13x365 = 4745)
product_service_cost = 2000;		# Servicing cost after repairing faulty product
ad_sponsor_amount = 5000			# Sponsorship Amount (Source of Income) After 0.7 popularity

# total_investment = 91195200		# initial amount needed to manufacture 4800 products
total_investment = 150000000		# initial amount needed to manufacture 4800 products
total_revenue = 0					
total_profit = 0
failure_stories = 0
total_revenue_per_day = []

y = []
x = []

# This Function Calls for Repair and updates popularity
def callRepair():
	global person_product, product_popularity, total_revenue, failed_product, product_service_cost

	for i in range(len(person_product)):
		if person_product[i][0].isFailed:
			failed_product += 1
			total_revenue -= (person_product[i][0].total_cost + person_product[i][0].profit + product_service_cost)
			print("----FAULTY PRODUCT----")
			person_product[i][0].isFailed = not bool(randint(0,10)%10)

# This function alters product cost
def updateProductCost():
	global product_sold, total_cost_per_product, profit_per_product, GAIN_FACTOR

	if total_profit < 0:
		if product_sold%1000 == 0 and total_cost_per_product + profit_per_product <= 25000:
			profit_per_product += GAIN_FACTOR
	elif total_profit >= 0:
		if product_sold%500 == 0 and total_cost_per_product + profit_per_product >= 16999:
			profit_per_product -= GAIN_FACTOR
			if profit_per_product < 500:
				profit_per_product = 500

# This function alters product popularity
def alterPopularity():
	global product_sold, product_popularity, failed_product
	product_popularity = float(0.444 + (1.111/math.pi)*math.atan(((product_sold - 100*failed_product)/1000)-0.75))

	# Converting to 4 decimal places
	product_popularity *= 10000
	product_popularity = int(product_popularity)
	product_popularity = float(product_popularity/10000)

# Creates the Total Revenue array for graphs
def updateMarketStatus():
	global product_sold, total_revenue, total_profit, total_investment, profit_per_product, total_cost_per_product, GAIN_FACTOR, rate_product_sold, x, y, product_popularity, ad_sponsor_amount

	# calculating the revenue
	if product_sold <= 4800:
		total_revenue += total_cost_per_product + profit_per_product
	else:
		total_revenue += profit_per_product
	
	# Sponsor Branding Amount
	if product_popularity > 0.5:
		total_revenue += ad_sponsor_amount

	total_profit = total_revenue - total_investment

	print("Product: "+str(product_sold)+" | Total Profit: "+str(total_profit)+" | Product Popularity: "+str(product_popularity)+" | Product Cost: "+str(total_cost_per_product + profit_per_product))
	y.extend([total_profit])
	x.extend([int(product_sold/production_limit_per_day)])

	alterPopularity()
	updateProductCost()

# Generates results for per day basis
def GenerateResultsPerDay(product_sold_that_day):
	global total_revenue_per_day, y
	total_revenue_per_day.extend([y[product_sold_that_day]])