 import numpy as np
import matplotlib.pyplot as plt

# House prices data
house_prices = [300000, 350000, 320000, 280000, 400000, 380000, 330000, 310000, 290000, 270000, 350000, 380000, 370000]

mean_price = np.mean(house_prices)
print("Mean Price: ",mean_price)

median_price = np.median(house_prices)
print("Median Price: ,",median_price)

mode_price = np.argmax(np.bincount(house_prices))
print("Mode Price:", mode_price)

std_deviation = np.std(house_prices)
print("Standard Deviation:",std_deviation)

plt.boxplot(house_prices)
plt.xlabel('House Prices')
plt.ylabel('Price')
plt.title('Distribution of House Prices')
plt.show()
