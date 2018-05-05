import math
from random import randint

total_cost_per_product = 18999
profit_per_product = 2000
product_sold = 0
failed_product = 0				# Number of failed products
rate_product_sold = 4800		# rate of product sold per week
person_product = []
GAIN_FACTOR = 500				# After every 1000 sold products
product_popularity = 0.05
production_limit_per_day = 20;
product_service_cost = 2000;

# total_investment = 91195200		# initial amount needed to manufacture 4800 products
total_investment = 150000000		# initial amount needed to manufacture 4800 products
total_revenue = 0
total_profit = 0
failure_stories = 0
total_revenue_per_day = []

y = []
x = []

# DEBUG PURPOSE
def showProductPerson():
	global person_product
	for i in range(len(person_product)):
		if person_product[i][0].isFailed:
			print("Person ID: "+str(person_product[i][1])+" | Product cost: "+str(person_product[i][0].total_cost + person_product[i][0].profit)+" | Fail status: "+str(person_product[i][0].isFailed))

def callRepair():
	global person_product, product_popularity, total_revenue, failed_product, product_service_cost

	for i in range(len(person_product)):
		if person_product[i][0].isFailed:
			failed_product += 1
			total_revenue -= (person_product[i][0].total_cost + person_product[i][0].profit + product_service_cost)
			print("----FAULTY PRODUCT----")
			person_product[i][0].isFailed = not bool(randint(0,10)%10)

def updateProductCost():
	global product_sold, total_cost_per_product, profit_per_product, GAIN_FACTOR

	if total_profit < 0:
		if product_sold%1000 == 0 and total_cost_per_product + profit_per_product <= 25000:
			total_cost_per_product += GAIN_FACTOR
			profit_per_product += GAIN_FACTOR
	elif total_profit >= 0:
		if product_sold%500 == 0 and total_cost_per_product + profit_per_product >= 16999:
			total_cost_per_product -= GAIN_FACTOR
			profit_per_product -= GAIN_FACTOR



def alterPopularity():
	global product_sold, product_popularity, failed_product
	product_popularity = float(0.444 + (1.111/math.pi)*math.atan(((product_sold - 120*failed_product)/1000)-2))


def updateMarketStatus():
	global product_sold, total_revenue, total_profit, total_investment, profit_per_product, total_cost_per_product, GAIN_FACTOR, rate_product_sold, x, y, product_popularity

	# calculating the revenue
	total_revenue += total_cost_per_product + profit_per_product
	
	total_profit = total_revenue - total_investment

	print("Product: "+str(product_sold)+" | Total Profit: "+str(total_profit)+" | Product Popularity: "+str(product_popularity)+" | Product Cost: "+str(total_cost_per_product + profit_per_product))
	y.extend([total_profit])
	x.extend([int(product_sold/production_limit_per_day)])

	alterPopularity()
	updateProductCost()


def GenerateResultsPerDay(product_sold_that_day):
	global total_revenue_per_day, y
	total_revenue_per_day.extend([y[product_sold_that_day]])