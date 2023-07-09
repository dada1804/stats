import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

# Read the dataset
data = pd.read_csv("adver_sales.csv")  # Replace "sales_dataset.csv" with the actual file name

# Extract sales revenue and advertising expenditure columns
sales_revenue = data['sales_revenue']
advertising_expenditure = data['advertising_expenditure']

# Calculate the Karl Pearson correlation coefficient
correlation_coefficient, p_value = pearsonr(sales_revenue, advertising_expenditure)

# Interpret the correlation coefficient
if correlation_coefficient > 0:
    correlation_direction = "positive"
elif correlation_coefficient < 0:
    correlation_direction = "negative"
else:
    correlation_direction = "no"

correlation_strength = abs(correlation_coefficient)

# Print the results
print("Correlation Coefficient:", correlation_coefficient)
print("Correlation Direction:", correlation_direction)
print("Correlation Strength:", correlation_strength)

# Visualize the relationship using a scatter plot
plt.scatter(advertising_expenditure, sales_revenue)
plt.xlabel("Advertising Expenditure")
plt.ylabel("Sales Revenue")
plt.title("Relationship between Advertising Expenditure and Sales Revenue")
plt.show()

