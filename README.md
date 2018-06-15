# Product Sales Simulation

## Introduction
This project aimed to create a real-life (almost) analysis of how a product would sell in an Indian market comprising various types of population. This was a helper project in my course *Innovation & Entrepreneurship* during semester 6 (Q1-2 2018).
This python based project used Matplot Lib to plot the results obtained as day-wise & sales-wise graphs. Other than that it exports the data in a usable CSV format.

Three type of population is considered in this analysis
1. Highly Rich Class - They can buy more than one product & have high will to buy the product.
2. Rich Class - They can buy more than one product but have intermediate will to buy & threshold.
3. Medium Class - They will only buy one product & only when popularity hits a certain level.

### Project Report
This is the non-technical project report of the course.
[Final_report.pdf](https://github.com/shubham1chawla/Product-Simulation/files/2106239/Final_report.pdf)

### Business Model Canvas
![poster](https://user-images.githubusercontent.com/31181262/41469516-1dd204cc-70cb-11e8-980d-34071a64f18b.png)

The above mentioned BMC was implemented in the sales simulation software. All the constraints are considered with respect to the BMC and implementation of this BMC in Indian Market.

### Output Plot
***Matplot Lib is used for the plots. Install Matplot Library before compiling the index.py file.***
![sketch](https://user-images.githubusercontent.com/31181262/41469725-ffc9d684-70cb-11e8-9efe-31b6155a9727.png)

The output obtained contains two plot, first one with product-sales wise analysis and second one with day-wise analysis versus the total profit. Total profit is calculated by subtracting Total money gained on product sales and Total initial investment. The Yellow line axis gives us **no-profit-no-loss** or **break-away point**. The red dots on the day-wise analysis curve gives us the info of years passed.

## How to use

- After fetching the code, use index.py to build the application. You may encounter a small delay before sales info comes on your terminal. 
- Incase you encounter error, rebuild the project again. Matplot Lib is necessary to complete the compilation without errors.
- All the configuration variables and constants are in Market.py file. Alter them at your own risk. Ruppee was considered as the medium of money for the analysis.